#downloaded files mover to a categorized folder.
#this py file will also be moved after this program ran if this is on the same source directory
#looks like this program doesnt need root permissions
"""
cd Downloads
python file_dl_mover.py

I dont include .html into the program_formatname list because sometimes when you download html it is tied to a folder for the html assets.
"""

import os
import shutil  # For moving files

def dlmove(sourceDir, targetDir):
    compressed_formatname = ['.zip', '.7z', '.rar']
    image_formatname = ['.jpg', '.jpeg', '.png', '.ico', '.webm', '.gif']
    doc_formatname = ['.txt', '.pdf', '.xls', '.xlsx', '.doc', '.docx']
    program_formatname = ['.exe', '.py', '.bat', '.dll', '.cpp', '.msi']

    with os.scandir(sourceDir) as items:
        for item in items:
            #print(item.name)
            if item.is_file():  # Process only files, not directories
                name = item.name
                source_path = item.path
                #checks if the file ends with any extension in the list
                if any(name.endswith(ext) for ext in compressed_formatname):
                    try: #try-except block to catch and report errors during file moving.
                        # Construct the full source and destination paths
                        destination_path = os.path.join(targetDir[0], name)
                        # Move the file to the compressed directory
                        shutil.move(source_path, destination_path)
                        print(f"Moved: {name} -> {targetDir[0]}")
                    except Exception as e:
                        print(f"error moving {name}: {e}")
                elif any(name.endswith(ext) for ext in image_formatname):
                    try:
                        destination_path = os.path.join(targetDir[1], name)
                        shutil.move(source_path, destination_path)
                        print(f"Moved: {name} -> {targetDir[1]}")
                    except Exception as e:
                        print(f"error moving {name}: {e}")
                elif any(name.endswith(ext) for ext in doc_formatname):
                    try:
                        destination_path = os.path.join(targetDir[2], name)
                        shutil.move(source_path, destination_path)
                        print(f"Moved: {name} -> {targetDir[2]}")
                    except Exception as e:
                        print(f"error moving {name}: {e}")
                elif any(name.endswith(ext) for ext in program_formatname):
                    try:
                        destination_path = os.path.join(targetDir[3], name)
                        shutil.move(source_path, destination_path)
                        print(f"Moved: {name} -> {targetDir[3]}")
                    except Exception as e:
                        print(f"error moving {name}: {e}")

                # Log unhandled files
                else:
                    print(f"Unhandled file: {name}")

def dlmover_directory_check():
    #insert your windows username. directories are tied to usernames.
    username = input("insert your username for this device:")
    WINDOWS_USERNAME = username
    
    #use fr because we want to insert username. just use r otherwise. r is so it is reads as string
    source_directory = fr"C:\Users\{WINDOWS_USERNAME}\Downloads"
    compressed_directory = fr"C:\Users\{WINDOWS_USERNAME}\Downloads\dl-compressed"
    image_directory = fr"C:\Users\{WINDOWS_USERNAME}\Downloads\dl-img"
    document_directory = fr"C:\Users\{WINDOWS_USERNAME}\Downloads\dl-docs"
    program_directory = fr"C:\Users\{WINDOWS_USERNAME}\Downloads\dl-programs"

    target_directories = [compressed_directory, image_directory, document_directory, program_directory]

    # Ensure directories exist
    if os.path.exists(source_directory):
        print(f"Source directory ({source_directory}) exists.")
    else:
        print(f"Source directory ({source_directory}) does not exist.")
    for directory in target_directories:
        os.makedirs(directory, exist_ok=True)
        print(f"[checking]: {directory}")

    dlmove(source_directory, target_directories);

dlmover_directory_check()