import os
from termcolor import colored


''' If given a directory, @returns the previous sibling directory (sorted alphabetically) in the same directory as the given directory.
    If given a file, it uses the parent directory of the file to find the previous sibling directory.
'''
def getPrevDirPath(uri):
    if not os.path.isdir(uri):
        dir_uri = os.path.dirname(uri)
    else: dir_uri = uri
    

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

    # Return the previous directory if it exists, otherwise return None
    file_name = siblings_alpha[current_index - 1] if current_index > 0 else None
    
    file_path = os.path.join(parent_dir, file_name) if file_name else None
    
    
    return file_path
  
  
  
# EXAMPLES
 
# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/system1/segments/t4_mutateData/"
# prev_dir_path = getPrevDirPath(path)
# print(prev_dir_path)

# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/system1/segments/t4_mutateData/a_addHashCol.py"
# prev_dir_path = getPrevDirPath(path)
# print(prev_dir_path)


# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipes/single_pipelines/system1/segments/pre1_setupData"
# prev_dir_path = getPrevDirPath(path)
# print(prev_dir_path)

# # example where there is no previous directory
# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipes/single_pipelines/system1/segments/archive"
# prev_dir_path = getPrevDirPath(path)
# print(prev_dir_path)