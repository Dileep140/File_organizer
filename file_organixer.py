import os
import datetime

def organize_files_by_extension(source_path):
    """Organizes files in the specified directory based on their file extensions.

    Args:
        source_path (str): The path to the directory containing the files to be organized.
    """
    # List to store unique file extensions
    unique_extensions = []

    # Scan the specified directory for files
    items = os.listdir(source_path)

    for item in items:
        full_path = os.path.join(source_path, item)

        # Check if the item is a file
        if os.path.isfile(full_path):
            # Extract file extension
            file_extension = os.path.splitext(full_path)[1]

            # Add unique extensions to the list
            if file_extension not in unique_extensions:
                unique_extensions.append(file_extension)

    # Create directories based on unique file extensions
    for extension in unique_extensions:
        directory_name = extension[1:]  # Remove the dot from the extension
        dir_path = os.path.join(source_path, directory_name)

        try:
            os.makedirs(dir_path)
            print(f"Directory '{directory_name}' created.")
        except FileExistsError:
            print(f"Directory '{directory_name}' already exists.")
        except PermissionError:
            print(f"Permission denied to create directory '{directory_name}'.")
        except Exception as e:
            print(f"An error occurred while creating directory '{directory_name}': {str(e)}")

    # Log the activity
    log_activity(source_path, unique_extensions)

def move_files_to_directories(source_path):
    """Moves files in the specified directory to directories based on their file extensions.

    Args:
        source_path (str): The path to the directory containing the files to be moved.
    """
    # List to store moved file names
    moved_files = []

    # Scan the specified directory for files
    file_names = os.listdir(source_path)

    for file_name in file_names:
        full_path = os.path.join(source_path, file_name)

        # Check if the item is a file
        if os.path.isfile(full_path):
            # Extract file extension
            file_extension = os.path.splitext(full_path)[1]

            # Create destination path with directory and filename
            destination = os.path.join(source_path, file_extension[1:], file_name)

            # Move the file
            os.rename(full_path, destination)

            # Add moved file to the list
            moved_files.append(file_name)

    # Log the activity
    log_activity(source_path, moved_files, action='move')

def log_activity(source_path, items, action='create'):
    """Logs the activity of creating directories or moving files.

    Args:
        source_path (str): The path to the directory.
        items (list): List of items (directories or files) involved in the activity.
        action (str): The type of activity ('create' or 'move').
    """
    log_file_path = os.path.join(source_path, "activity_log.txt")

    with open(log_file_path, "a") as log_file:
        timestamp = datetime.datetime.now()
        log_file.write(f"{timestamp} - {action.capitalize()} activity in '{source_path}': {items}\n")

if __name__ == "__main__":
    target_directory = r"Enter the path of directory"

    # Organize files by extension
    organize_files_by_extension(target_directory)

    # Move files to directories
    move_files_to_directories(target_directory)
