import os
import boto3
from datetime import datetime

def get_latest_backup(directory):
  """
  Gets the path to the latest backup file in a directory.

  Args:
      directory: Path to the directory containing backup files.

  Returns:
      Path to the latest backup file, or None if no backups found.
  """

  # Get all files in the directory sorted by modification time (descending)
  files = sorted(os.listdir(directory), key=os.path.getmtime, reverse=True)
  for filename in files:
    # Check if the filename starts with "backup_" (assuming backup files follow this naming convention)
    if filename.startswith("trial_"):
      return os.path.join(directory, filename)
  return None

def upload_file_to_s3(file_path, bucket_name, s3_file_name):
  """
  Uploads a file from the local system to an S3 bucket.

  Args:
      file_path: Path to the local file.
      bucket_name: Name of the S3 bucket.
      s3_file_name: Name of the file within the S3 bucket.
  """

  # Create an S3 client
  s3 = boto3.client('s3')

  # Upload the file
  try:
    s3.upload_file(file_path, bucket_name, s3_file_name)
    print(f"Successfully uploaded {file_path} to s3://{bucket_name}/{s3_file_name}")
  except FileNotFoundError:
    print(f"Error: File not found - {file_path}")
  except Exception as e:
    print(f"Error uploading file: {e}")

# Replace with your credentials and directory information
bucket_name = "erpdatabackup"
backup_directory = "C:/Users/USER/Desktop"
s3_file_name_prefix = "trial_"  # Optional: Prepend this to the uploaded filename

# Find the latest backup file
latest_backup = get_latest_backup(backup_directory)

if latest_backup:
  # Construct the S3 filename (optional: add timestamp)
  s3_file_name = f"{s3_file_name_prefix}{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.tar.gz"  # Replace with your desired format
  upload_file_to_s3(latest_backup, bucket_name, s3_file_name)
else:
  print("No backup files found in the specified directory.")
