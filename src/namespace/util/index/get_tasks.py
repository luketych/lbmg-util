import os

# TODO Update this so that it instead of printing "Scripts to execute:
# s0__fetchData/c__fetchSubIDdaily.py
# split1__campaignDaily/a__renameCols.py
# .. it will print "s1__/split1__campaignDaily/a__renameCols.py"
def get_tasks(directory="./segments", ignore_starts_with=["x_", "archive"], ignore_ends_with=["_x"]):
    """
    Get a list of ordered files in the specified directory, excluding certain files based on prefixes and suffixes.

    Parameters:
    - directory (str, optional): The directory to search for files. Default is "./tasks".
    - ignore_starts_with (list, optional): List of prefixes to ignore. Default is ["x_"].
    - ignore_ends_with (list, optional): List of suffixes to ignore. Default is ["_x"].

    Returns:
    - list: List of ordered files.
    """
    
    ordered_files = []
    

    for root, dirs, files in os.walk(directory):
        # Ignore the "archive" directory and its contents
        if "archive" in dirs:
            dirs.remove("archive")


        for file in files:
            if (
                (root.endswith("tasks") and file not in ["index.py", "index.sh"]) or
                (not file.startswith(".") and not file.startswith("index.") and
                 not (ignore_starts_with and any(file.startswith(prefix) for prefix in ignore_starts_with)) and
                 not (ignore_ends_with and any(file.endswith(suffix) for suffix in ignore_ends_with)) and
                 (file.endswith(".py") or file.endswith(".sh")))
            ):
                file_path = os.path.join(root, file)
                ordered_files.append(file_path)

    ordered_files.sort()
    
    # remove any files that are in a dir that is prefixed with archive, or x_
    ordered_files = [file for file in ordered_files if not any([f"/archive/" in file, f"/x_" in file])]
    
    
    return ordered_files