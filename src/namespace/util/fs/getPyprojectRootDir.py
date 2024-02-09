import os


"""
Get the root directory of the project.
It is difficult to know what is the project root, so instead we will look for the pyproject.toml file.

Returns:
- str: The path of the root directory, or None if the root directory is not found.
"""
def getPyprojectRootDir():
    dir_path = os.path.dirname(__file__)
    current_path = os.path.abspath(dir_path)

    while True:
        # Check for the existence of pyproject.toml in the current directory
        pyproject_path = os.path.join(current_path, 'pyproject.toml')
        
        if os.path.isfile(pyproject_path):
            return current_path

        # Move to the parent directory
        parent_path = os.path.dirname(current_path)

        # Check if we have reached the root directory
        if parent_path == "/":
            return None

        current_path = parent_path