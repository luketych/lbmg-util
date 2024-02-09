import os


"""
Get the root directory of the project. 
Crawls up to the workspace dir looking for the highest directory that contains a pyproject.toml file.

Returns:
- str: The path of the root directory, or None if the root directory is not found.
"""
def getProjectRootDir():
    dir_path = os.path.dirname(__file__)
    current_path = os.path.abspath(dir_path)
    workspace_dir = os.path.join(current_path, "workspace")  # Define the workspace directory
    
    pyproject_paths = []

    while True:
        pyproject_path = os.path.join(current_path, 'pyproject.toml')
        
        if os.path.isfile(pyproject_path):
            dir_path = os.path.dirname(pyproject_path)
            pyproject_paths.append(dir_path)

        if current_path == workspace_dir:  # have we reached the workspace dir?
            # No pyproject.toml found within the workspace
            return pyproject_paths[-1] if pyproject_paths else None


        # Move to the parent directory
        parent_path = os.path.dirname(current_path)

        if parent_path == "/":  # have we reached the root dir?
            # return the last element of the list pyproject_paths or None if the list is empty
            return pyproject_paths[-1] if pyproject_paths else None

        current_path = parent_path


# Example usage
# root_dir = getProjectRootDir()
# if root_dir:
#     print("Root directory with pyproject.toml:", root_dir)
# else:
#     print("No pyproject.toml found within the workspace directory or its parents.")