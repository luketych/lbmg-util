import os

from .getPyprojectRootDir import getPyprojectRootDir


"""
    @return type: str - "absolute", "relative", "project-relative"
    @throws ValueError if the path does not exist
"""
def getPathType(path: str) -> str:
    """
    Returns the type of path, ie "absolute", "relative", "project-relative"
    """
    
    if path.startswith("/"):
        return "absolute"
      
    elif path.startswith("."):
        return "relative"
    
    else:
        abs_path = os.path.join(getPyprojectRootDir(), path)
        
        # check if the path exists
        if os.path.exists(abs_path):
            return "project-relative"
        else:
            raise ValueError("The path does not exist.")
    
    
    
    
# EXAMPLES

# path = "/a/b/c/d"
# path_type = getPathType(path)
# print(path_type)

# path = "../a/b/c/d"
# path_type = getPathType(path)
# print(path_type)

# path = "src/pipelines/single_pipelines/system1/config.json"
# path_type = getPathType(path)
# print(path_type)