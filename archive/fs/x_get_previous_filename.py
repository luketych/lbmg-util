import os




def is_valid_name(filename):
    # Function to check if the filename is valid (not __pycache__ or hidden)
    return not filename.startswith("__") and not filename.startswith(".")

def get_previous_filename(current_file_uri, allow_dirs=False):
    # Extract the directory and file name from the given path
    curr_dir_uri, current_file_name = os.path.split(current_file_uri)

    # Get the list of files in the directory (excluding invalid files and directories)
    files = sorted(file for file in os.listdir(curr_dir_uri) if is_valid_name(file) and os.path.isfile(os.path.join(curr_dir_uri, file)))

    # Find the index of the current file in the sorted list
    current_file_index = files.index(current_file_name)

    # Check if there is a file before the current file
    if current_file_index > 0:
        # Get the filename of the previous file
        previous_file_name = files[current_file_index - 1]
    else:
        # No previous file in the current directory, go to the parent directory
        parent_directory = os.path.dirname(curr_dir_uri)
        
        #parent_files = sorted(file for file in os.listdir(parent_directory) if is_valid_filename(file) and os.path.isfile(os.path.join(parent_directory, file)))

        # Filter files and directories based on allow_dirs parameter
        is_valid = lambda file: is_valid_name(file) and (allow_dirs or os.path.isfile(os.path.join(parent_directory, file)))

        parent_files = sorted(file for file in os.listdir(parent_directory) if is_valid(file))
        
        # filter for dirs
        parent_dirs = [file for file in parent_files if os.path.isdir(os.path.join(parent_directory, file))]
        
        # sort alpahbetically
        parent_dirs_alpha = sorted(parent_dirs)
        
        # get the previous dir from curr_dir_uri
        curr_dir = os.path.basename(curr_dir_uri)
        


        # Check if there are files in the parent directory
        if parent_files:
            # Get the filename of the last file in the parent directory
            previous_file_name = parent_files[-1]
        else:
            # No previous file found
            return None

    # Combine the directory and previous file name
    previous_file_path = os.path.join(curr_dir_uri, previous_file_name)

    return previous_file_path