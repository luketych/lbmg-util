import os

from .getPathType import getPathType
from .getPyprojectRootDir import getPyprojectRootDir


def getAbsPath(path: str) -> str:
    path_type = getPathType(path)
    
    if path_type == "absolute":
        return path
    elif path_type == "relative":
        return os.path.abspath(path)
    elif path_type == "project-relative":
        projectRootDirAbsPath = getPyprojectRootDir()
        return os.path.join(projectRootDirAbsPath, path)