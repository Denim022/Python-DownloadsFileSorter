import os
import shutil

EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".dmg", ".sh"],
    "Others": []  # Catch-all for uncategorized files
}

def create_folder(folder_name, base_path):
    """Create a folder if it does not exist."""
    folder_path = os.path.join(base_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def get_folder_name(extension):
    """Map file extension to folder name."""
    for folder, extensions in EXTENSION_MAP.items():
        if extension in extensions:
            return folder
    return "Others"  # Default folder for unknown extensions

def sort_downloads(directory):
    """Sort files in the Downloads folder into categorized folders."""
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # List all files in the directory
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Extract file extension
        file_extension = os.path.splitext(file)[1].lower()
        folder_name = get_folder_name(file_extension)
        
        # Create the target folder and move the file
        destination_folder = create_folder(folder_name, directory)
        shutil.move(file_path, os.path.join(destination_folder, file))
        print(f"Moved: {file} -> {destination_folder}")

if __name__ == "__main__":
    # Path to your Downloads folder
    downloads_folder = os.path.expanduser("~/Downloads")  # Here just replace  os.path.expanduser("~/Downloads") with your downloads folder directory. It works across almost all platforms
    sort_downloads(downloads_folder)
