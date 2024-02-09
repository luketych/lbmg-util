import os
from termcolor import colored


def get_next_dir_path(uri):
    is_dir = os.path.isdir(uri)

    if is_dir:
        # get parent dir
        dir_uri = os.path.dirname(uri)
    else:
        dir_uri = os.path.dirname(uri)
    

    parent_dir = os.path.dirname(dir_uri)
    

    # Get a list of all entries in the parent directory
    all_entries = os.listdir(parent_dir)

    # Filter directories from the list
    sibling_dirs = [entry for entry in all_entries if os.path.isdir(os.path.join(parent_dir, entry))]

    siblings_alpha = sorted(sibling_dirs)

    # Find the index of the current directory in the sorted list
    try:
        current_index = siblings_alpha.index(os.path.basename(dir_uri))
    except ValueError:
        print(f"The current directory {os.path.basename(dir_uri)} is not in the given URI.")
        return None

    # Return the next directory if it exists, otherwise return None
    dir_name = siblings_alpha[current_index + 1] if current_index < len(siblings_alpha) - 1 else None

    dir_path = os.path.join(parent_dir, dir_name) if dir_name else None

    return dir_path
  
  

# EXAMPLES
 
# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/system1/tasks/t4_mutateData/"
# next_dir_path = get_next_dir_path(path)
# print(next_dir_path)

# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/system1/tasks/t4_mutateData/a_addHashCol.py"
# next_dir_path = get_next_dir_path(path)
# print(next_dir_path)