import os
import datetime


def create_log_entry(message, source_directory):
    """Creates a log entry with the current timestamp, the specified message,
    and saves it to a log file in the source directory.

    Args:
        message: The message to be logged.
        source_directory: The path to the directory containing the files to be organized.
    """
    log_file_path = os.path.join(source_directory, "file_organizer.log")
    if not os.path.exists(source_directory):  # Ensure the source directory exists
        os.makedirs(source_directory)
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {message}\n")

def create_directories_by_extension(source_directory):
    """Creates directories based on file extensions in the specified directory.

    Args:
        source_directory: The path to the directory containing the files to be organized.
    """

    unique_extensions = set()
    for item in os.listdir(source_directory):
        full_path = os.path.join(source_directory, item)
        if os.path.isfile(full_path):
            file_extension = os.path.splitext(full_path)[1]
            unique_extensions.add(file_extension)

    for extension in unique_extensions:
        try:
            os.makedirs(os.path.join(source_directory, extension[1:]))
            create_log_entry(f"Directory created for extension: {extension}", source_directory)
        except FileExistsError:
            create_log_entry(f"Directory for extension '{extension}' already exists.", source_directory)
        except PermissionError:
            create_log_entry(f"Permission denied to create directory for extension '{extension}'.", source_directory)
        except Exception as e:
            create_log_entry(f"Error creating directory for extension '{extension}': {str(e)}", source_directory)


def move_files(source_directory):
    """Moves files to directories based on their extensions, excluding the log file.

    Args:
        source_directory: The path to the directory containing the files to be organized.
    """

    moved_files = []
    for item in os.listdir(source_directory):
        full_path = os.path.join(source_directory, item)
        if os.path.isfile(full_path) and item != "file_organizer.log":  # Exclude the log file
            file_name = os.path.basename(full_path)
            file_extension = os.path.splitext(full_path)[1]
            destination_directory = os.path.join(source_directory, file_extension[1:])
            destination_path = os.path.join(destination_directory, file_name)
            os.rename(full_path, destination_path)
            moved_files.append(file_name)

    create_log_entry(f"Files moved: {moved_files}", source_directory)



if __name__ == "__main__":
    source_path = r"F:\Face Mask detection"
    create_directories_by_extension(source_path)
    move_files(source_path)
