import os
import paramiko
from scp import SCPClient
import subprocess

package = "package.tar.gz"

def upload_source(local_path, remote_path, host, port, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=user, password=password)

    subprocess.Popen(["tar", "-czf", package, "-C", local_path, "."]).wait()
    
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(package, os.path.join(remote_path, package))
        stdin, stdout, stderr = ssh.exec_command(f"cd {remote_path} && tar -xzf {package}")
        stdout.channel.recv_exit_status()  # Wait for the command to complete

        print("stderr: ", stderr.read().decode())

        ssh.exec_command(f"rm {os.path.join(remote_path, package)}")
    
    print("All files uploaded successfully.")
    
    ssh.close()
