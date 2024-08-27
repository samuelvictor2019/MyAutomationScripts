# import paramiko

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='', username='', password='', port=)
# sftp_client=ssh.open_sftp()

# sftp_client.get('path/to/remote/file', 'filename')


# sftp_client.close()
# ssh.close()



import paramiko

# Define the remote machine's details
remote_machine_ip = "remote_machine_ip"
remote_machine_username = "remote_machine_username"
remote_machine_password = "remote_machine_password"
remote_machine_file_directory = "/remote-machine-file-directory/"

# Define the local file to be sent
local_file_path = "/local-file-path/"

# Establish an SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(remote_machine_ip, username=remote_machine_username, password=remote_machine_password)

# Open an SFTP client
sftp = ssh.open_sftp()

# Send the file
sftp.put(local_file_path, remote_machine_file_directory)

# Close the SFTP and SSH connections
sftp.close()
ssh.close()

