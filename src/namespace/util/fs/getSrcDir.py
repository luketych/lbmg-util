import os

from namespace.util import getPyprojectRootDir


"""
Keeps crawling up until it finds the src directory.

Args:
- starting_path (str): The starting path for crawling.

Returns:
- str: The path to the 'src' directory.
"""
def getSrcDir(starting_path: str = None, abs_or_rel: str = "rel") -> str:
  
    if starting_path is None:
        src_dir = os.path.join(getPyprojectRootDir(), "src")
        
        return src_dir
  
    current_dir = os.path.abspath(starting_path)

    while True:
        # Check if the current directory contains the 'src' directory
        src_dir = os.path.join(current_dir, "src")
        if os.path.exists(src_dir) and os.path.isdir(src_dir):
            return src_dir

        # Move up one directory level
        parent_dir = os.path.abspath(os.path.join(current_dir, ".."))

        # Break if the parent directory is the same as the current directory
        if parent_dir == current_dir:
            raise FileNotFoundError("'src' directory not found in the project.")

        current_dir = parent_dir



# Example usage:

# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/packages/util/src/fs/getPathTail.py"
# src_directory = getSrcDir(path)
# print(src_directory)

# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/packages/util/src/fs/"
# src_directory = getSrcDir(path)
# print(src_directory)

# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/single_pipelines/inuvo"
# src_directory = getSrcDir(path)
# print(src_directory)