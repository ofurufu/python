# Import os module to interact with the system
import os

# User enters dir(s) to see content
dirs = input("Please provide list of dir(s) with spaces inbetween: ").split()

# Looping through the dir(s)
for dir in dirs:
    try:
        files = os.listdir(dir)
    except FileNotFoundError:
        print(f"Error: Please enter a valid dir name in stead of {dir}.")
        continue
    except PermissionError:
        print("Error: You do not have permission to view content in this dir")
        continue
    
    print(f"\n====== Listing files in {dir} =====")
    
    # Count the number of files and print it
    count = len(files)
    if count == 0:
        print("(empty directory)")
    else:
        print(f"({count} item{'s' if count != 1 else ''})")
    
    # Looping through the files and print each file name
    for file in files:
        print(file)