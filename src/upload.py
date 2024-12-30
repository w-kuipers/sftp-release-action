import os
import paramiko
from scp import SCPClient

def upload_source(local_path, remote_path, host, port, user, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, port=port, username=user, password=password)
        
        with SCPClient(ssh.get_transport()) as scp:
            for root, dirs, files in os.walk(local_path):
                relative_path = os.path.relpath(root, local_path)

                dirpath = os.path.join(remote_path, relative_path)
                for dir in dirs:
                    stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {os.path.join(dirpath, dir)}")
                    stdout.channel.recv_exit_status()  # Wait for the command to complete

                for file in files:
                    local_file_path = os.path.join(root, file)
                    remote_file_path = os.path.join(remote_path, relative_path, file)
                    print(f"Uploading {local_file_path} to {remote_file_path}")
                    scp.put(local_file_path, remote_file_path)
        
        print("All files uploaded successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        ssh.close()
