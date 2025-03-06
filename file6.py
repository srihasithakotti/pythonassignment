import os
file_path = 'sample.txt'  

if os.access(file_path, os.R_OK):
    print(f"The file '{file_path}' has read access.")
else:
    print(f"The file '{file_path}' does NOT have read access.")
if os.access(file_path, os.W_OK):
    print(f"The file '{file_path}' has write access.")
else:
    print(f"The file '{file_path}' does NOT have write access.")
