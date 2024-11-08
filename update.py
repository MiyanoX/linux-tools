import paramiko
import pandas as pd
import os

# Load the software list
software_list = pd.read_csv('./Software_List_v2.csv')

# SFTP connection details
hostname = '30.61.33.6'
port = 22  # Default SFTP port
username = 'tencent'
password = 'tencent'
remote_directory = '/var/www'

# Initialize the SFTP client
try:
    # Create a transport object
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, password=password)
    
    # Initialize the SFTP client
    sftp = paramiko.SFTPClient.from_transport(transport)
    
    # Upload files
    for _, row in software_list.iterrows():
        local_path = row['location']
        remote_path = os.path.join(remote_directory, row['display_name'])
        
        try:
            sftp.put(local_path, remote_path)
            print(f"Uploaded {local_path} to {remote_path}")
        except FileNotFoundError:
            print(f"File not found: {local_path}")
    
    # Close the SFTP client and transport
    sftp.close()
    transport.close()
    print("Upload completed.")
    
except Exception as e:
    print(f"An error occurred: {e}")
