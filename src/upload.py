import os
import paramiko
from scp import SCPClient

def upload_source(local_path, remote_path, host, port, user, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        ssh.connect(hostname=host, port=port, username=user, password=password)

        local_path = os.path.abspath(local_path)
        
        # Use SCP to copy files
        with SCPClient(ssh.get_transport()) as scp:
            # for root, dirs, files in os.walk(local_path):
            #     # Construct relative path
            #     relative_path = os.path.relpath(root, local_path)
            #     remote_path = os.path.join(remote_path, relative_path)
            #
            #     # Create remote directories if they don't exist
            #     stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {remote_path}")
            #     stdout.channel.recv_exit_status()  # Wait for the command to complete
            #
            #     # Upload files
            #     for file in files:
            #         local_file_path = os.path.join(root, file)
            #         remote_file_path = os.path.join(remote_path, file)
            #         print(f"Uploading {local_file_path} to {remote_file_path}")
            #         scp.put(local_file_path, remote_file_path)


        
        print("All files uploaded successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        ssh.close()
