import os 

folder_path = "files_folder"

files = os.listdir(folder_path) 
count = 1 

for file in files:
    old_path = os.path.join(folder_path, file) 
    new_name = f"file_{count}.txt"
    new_path = os.path.join(folder_path, new_name) 
    
    os.rename(old_path, new_path) 
    count += 1 
print("All files renamed automatically!")
