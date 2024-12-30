import paramiko
import os

####
# Empty the destination directory via SSH
####

def clean_dest(host:str, port:int, user:str, password:str, path:str):

    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    print(host, port, user,password,path )
    ssh_client.connect(hostname=host, port=port, username=user, password=password)

    p1  = os.path.join(path, "*")
    p2  = os.path.join(path, ".[!.]*")
    p3  = os.path.join(path, "..?*")

    # Command to remove the file
    command = f"rm -rf {p1} {p2} {p3}"
    _, stdout, stderr = ssh_client.exec_command(command)
    stdout.channel.recv_exit_status()  # Wait for the command to complete

    # Print the output and any errors
    print("Output:", stdout.read().decode())
    print("Error:", stderr.read().decode())

    # Close the connection
    ssh_client.close()
