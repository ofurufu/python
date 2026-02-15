# Import os module to interact with the system
import os

# User enters dir(s) to see content
folders = input("Please provide list of dir(s) with spaces inbetween: ").split()

# Looping through the dir(s)
for folder in folders:
    file = os.listdir(folder)
    print(file)