import os
from variable import script_variables
import time

# # Step 3: Read the file as a string
# file_path = "./initial.yaml"
# with open(file_path, "r") as file:
#     file_content = file.read()

# # Step 4: Replace placeholders in the file content using string formatting
# file_content = file_content.format(**script_variables)
# print(file_content)

# # Step 5: Store the modified string into a new file
# output_file_path = "path/to/your/output_file.txt"
# with open(output_file_path, "w") as output_file:
#     output_file.write(file_content)

# print("Variables replaced and saved in the output file.")


import shutil

# Define the directory to store backups
backup_directory = "tmp"

# List of files to process
files_to_process = [
  "initial.yaml", 
  "inventory.yaml", 
  "master/keepalived.conf",
  "slave/keepalived.conf",
  "check_apiserver.sh",
  "haproxy.cfg",
]

# Create a backup directory if it doesn't exist
os.makedirs(backup_directory, exist_ok=True)

# Backup the original files
for file_path in files_to_process:
    # Calculate the path in the backup directory
    backup_path = os.path.join(backup_directory, file_path)

    # Create parent directories if they don't exist
    os.makedirs(os.path.dirname(backup_path), exist_ok=True)

    # Backup the original file
    shutil.copy(file_path, backup_path)

print("1")
time.sleep(10)

for file_path in files_to_process:
    with open(file_path, "r") as file:
        file_content = file.read()
    
    # Replace placeholders with variable values
    for key, value in script_variables.items():
        file_content = file_content.replace(f"{{{key}}}", value)
    # Save the updated content back to the same file or different output file
    with open(file_path, "w") as file:
        file.write(file_content)


print("2")
time.sleep(10)

# Restore original files from the backup directory
for file_name in files_to_process:
    original_path = os.path.join(backup_directory, file_name)
    if os.path.exists(original_path):
        shutil.copy(original_path, file_name)
