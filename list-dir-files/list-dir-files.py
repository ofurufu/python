# Import os module to interact with the system
import os

# User enters dir(s) to see content
dirs = input("Please provide list of dir(s) with spaces inbetween: ").split()

# Looping through the dir(s)
for dir in dirs:
    try:
        files = os.listdir(dir)
    except FileNotFoundError:
        print(f"Please enter a valid dir name in stead of {dir}.")
        continue
    except PermissionError:
        print("You do not have permission to view content in this dir")
        continue
    
    print(f"====== Listing files in {dir} =====")
    
    for file in files:
        print(file)