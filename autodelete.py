#!/bin/bash

# Set the backup directory
backup_dir=""

# Count the number of backups
num_backups=$(ls -1 "$backup_dir" | wc -l)

# If there are more than 5 backups, delete the oldest
if [ $num_backups -gt 5 ]; then
  oldest_backup=$(ls -1t "$backup_dir" | tail -1)
  rm "$backup_dir/$oldest_backup"
fi

