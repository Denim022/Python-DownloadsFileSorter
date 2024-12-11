# Automatic Folder Sorter:
This Python script organizes files in the users downloads folder into categorized subfolders based on file types (e.g., Images, Documents, Videos). It allows users to input the directory they wish to sort at runtime.

# Features:
Prompts the user to specify the folder to sort.
Automatically creates folders for file categories (e.g., Images, Documents, Videos).
Moves files into their respective folders based on file extensions.
Customizable extension-to-folder mapping.

# Prerequisites:
Python Installation:
Ensure you have Python installed on your system. Download it from python.org and also you need to have vs code.

# Dependencies:
This script does not require any external libraries. It uses Python’s built-in libraries (os, shutil).

# Setup:
Clone or Create the Script
Save the script as sort_files.py.

# Customize File Categories (Optional):
You can modify the EXTENSION_MAP dictionary in the script to include or remove file types as needed.

# How to Run:
1. Open a terminal (Command Prompt or Visual Studio Code terminal).
2. Navigate to the directory where the code file is saved
```   
  cd path\to\script\directory
```
3. Run the script:
```
   python sort_downloads.py
```
4. Enter the path to the folder you want to sort when prompted:
```
   Enter the path to the folder you want to sort: C:\Users\YourUsername\Downloads
```
The script will scan the folder and sort files into categorized subfolders.

# Scheduling the Script (Optional):

1. Windows (Task Scheduler)
You can schedule the script to run automatically:

Open Task Scheduler and create a new task.
 i. Set the Trigger (e.g., daily at a specific time).
 ii. Set the Action to run Python with the script:
```
python path\to\sort_downloads.py
```
# Enjoy a cleaner and more organized folder!

-Denim
