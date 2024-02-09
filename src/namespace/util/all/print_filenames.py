import os


def print_filenames(file_paths, print_immedate_dir=False):
    if not file_paths:
        print("Warning: The list of file paths is empty.")
    else:
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            if print_immedate_dir:
                first_dir = os.path.dirname(file_path).split("/")[-1]
                print(f"{first_dir}/{file_name}")
            else:
                print(file_name)