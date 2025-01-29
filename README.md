# Automatic Folder Sorter:
This Python script organizes files in the user's downloads folder into categorized subfolders based on file types (e.g., Images, Documents, Videos). It allows users to input the directory they wish to sort at runtime.

# Features:
Prompts the user to specify the folder to sort.
Automatically creates folders for file categories (e.g., Images, Documents, Videos).
Moves files into their respective folders based on file extensions.
Customizable extension-to-folder mapping.

# Prerequisites:
Python Installation:
Ensure you have Python installed on your system. Download it from python.org.

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

1. In the Windows Task Scheduler, create a new task.
2. In the "General" tab, enter the name of the task and select how often you want it to run.
3. In the "Triggers" tab, select "New."
4. In the "Begin the task" drop-down, select "On a schedule."
5. In the "Settings" section, select "Daily" and enter the time you want the task to run.
6. In the "Actions" tab, select "New."
7. In the "Action" drop-down, select "Start a program."
8. In the "Program/script" field, enter the full path to the Python interpreter, such as "C:\Python27\python.exe."
9. In the "Add arguments (optional)" field, enter the full path to the "sort_downloads.py" file.
10. Click "OK" to save the task.

# Enjoy a cleaner and more organized folder!

-Denim
