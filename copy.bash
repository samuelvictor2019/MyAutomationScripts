#!/bin/bash

# Source directory
src_dir="~/home/frappe_bench/sites/demo.local/private/backups"

# External drive directory
ext_drive="../autobackup"

# Ensure the external drive directory exists
if [ ! -d "$ext_drive" ]; then
  echo "External drive directory not found."
  exit 1
fi

# Function to check the number of pairs on the external drive
check_pair_count() {
  local file_count=$(ls -1 "$ext_drive"/*.sql.gz 2>/dev/null | wc -l)
  echo "$file_count"
}

# Function to delete the oldest pair on the external drive
delete_oldest_pair() {
  local oldest_pair=$(ls -1t "$ext_drive"/*.sql.gz | tail -n 1)
  if [ -n "$oldest_pair" ]; then
    rm "$oldest_pair" "$oldest_pair".json
    echo "Deleted the oldest pair: $oldest_pair"
  fi
}

# Function to check the file size and throw an alert
check_file_size() {
  local file="$1"
  local min_size=1073741824  # 1GB in bytes
  local file_size=$(stat -c %s "$file")

  if [ "$file_size" -lt "$min_size" ]; then
    notify-send "File Size Alert" "The backup file $file is less than 1GB."
  fi
}

# Sort the source directory by creation time and copy the latest pair
latest_pair=($(ls -1t "$src_dir"/*.sql.gz | head -n 1))
if [ -n "${latest_pair[0]}" ]; then
  cp "${latest_pair[0]}" "${ext_drive}"
  cp "${latest_pair[0]}".json "${ext_drive}"
  check_file_size "${latest_pair[0]}"
else
  echo "No .sql.gz files found in the source directory."
fi

# Check the number of pairs on the external drive
pair_count=$(check_pair_count)

# If there are more than 10 pairs, delete the oldest pair
if [ "$pair_count" -gt 10 ]; then
  delete_oldest_pair
fi

echo "Backup completed."
