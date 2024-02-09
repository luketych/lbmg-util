import os

from namespace.util import getPyprojectRootDir



project_root_dir = getPyprojectRootDir()


def getTestDir(start_path: str = None):
    """
    Get the path to the 'test' directory within the project where pyproject.toml is located.
    """
    
    if start_path is None:
        current_dir = os.path.abspath(os.path.dirname(__file__))
    else:
        # if start path is a file, get the directory of the file
        if os.path.isfile(start_path):
            current_dir = os.path.dirname(start_path)
        else:
            current_dir = start_path
    
    while True:
        # Check if the current directory contains a folder named "test"
        test_dir = os.path.join(current_dir, "test")
        
        if os.path.isdir(test_dir):
            return test_dir
          
        if current_dir == project_root_dir:
            return os.path.join(project_root_dir, "test")
          
        
        parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
        
        if parent_dir == current_dir:
            raise FileNotFoundError("pyproject.toml not found in the project directory.")
        
        current_dir = parent_dir
        
        
# EXAMPLES

# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/packages/pipelines/src/get_output_file_path.py"
# res = getTestDir(path)
# print(res)

# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/single_pipelines/system1/segments/s1_standardizeTables/split2_hourly/a_renameCols.py"
# res = getTestDir(path)
# print(res)