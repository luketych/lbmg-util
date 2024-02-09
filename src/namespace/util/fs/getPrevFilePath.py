import logging
import os
import sys
from termcolor import colored

from namespace.mylogging import createLogger
from .getProjectRootDir import getProjectRootDir

project_root_dir = getProjectRootDir()

current_file = os.path.basename(__file__)

# create full path from the project root directory and the tail
file_name = os.path.join(project_root_dir, "logs", current_file)

# TODO
logger = createLogger(__file__, filename=file_name, level=logging.DEBUG)


def is_hidden_file(entry):
    # Function to check if a file is hidden
    return entry.startswith('.')
  

def getPrevFilePath(file_uri, ignore_files=["index.py"], include_only_filetype=".py"):
    """
    Get the path of the previous file in the directory based on the given file URI.

    Parameters:
    - file_uri (str): The URI of the current file.
    - ignore_files (list, optional): List of file names to ignore when finding the previous file. Default is ["index.py"].
    - include_only_filetype (str, optional): Filter for files with the specified file type. Default is ".py".

    Returns:
    - str or None: The path of the previous file, or None if not found.
    """
    # Check if the given URI is a file
    if os.path.isdir(file_uri):
        print(colored(f"The given URI '{file_uri}' is a directory, not a file.", 'yellow'))
        return None

    parent_dir = os.path.dirname(file_uri)

    # Get a list of all entries in the parent directory
    try:
      all_entries = os.listdir(parent_dir)
    except FileNotFoundError:
      print(colored(f"The parent directory '{parent_dir}' does not exist.", 'yellow'))
      logger.warning(f"The parent directory '{parent_dir}' does not exist.")
      return None

    # Filter files based on file type and ignore the specified files
    sibling_files = [entry for entry in all_entries if
                     os.path.isfile(os.path.join(parent_dir, entry)) and
                     not is_hidden_file(entry) and
                     entry.endswith(include_only_filetype) and
                     entry not in ignore_files]

    siblings_alpha = sorted(sibling_files)

    # Find the index of the current file in the sorted list
    try:
        current_index = siblings_alpha.index(os.path.basename(file_uri))
    except ValueError:
        print(f"The current file {os.path.basename(file_uri)} is not in the given URI.")
        return None

    # Return the previous file if it exists, otherwise return None
    prev_file_name = siblings_alpha[current_index - 1] if current_index > 0 else None

    # Construct the full path to the previous file
    prev_file_path = os.path.join(parent_dir, prev_file_name) if prev_file_name else None

    return prev_file_path
  
  
  
# EXAMPLES
 
# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/system1/tasks/t4_mutateData/"
# prev_file_path = getPrevFilePath(path)
# print(prev_file_path)

# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/system1/tasks/t4_mutateData/a_addHashCol.py"
# prev_file_path = getPrevFilePath(path)
# print(prev_file_path)