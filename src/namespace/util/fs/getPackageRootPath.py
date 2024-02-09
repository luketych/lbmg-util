import os

from .getPyprojectRootDir import getPyprojectRootDir

    
"""
    @start_path: str - a path to a dir or file inside the package we want to find the root of
    @abs_or_prp: str - "abs" or "prp" - whether to return the absolute path or the project-relative path
"""
def getPackageRootPath(start_path, abs_or_prp: str = "prp"):
    """
    Get the root path of the package containing the given start_path.
    """
    
    current_path = os.path.abspath(start_path)
    
    packageRootAbsPath = ""

    while True:
        this_path = current_path
        current_path = os.path.dirname(current_path)
        current_dir = os.path.basename(current_path)
        
        if current_dir == "":
            break
        if current_dir == "packages":
            packageRootAbsPath = this_path
            

    if abs_or_prp == "abs":
        return packageRootAbsPath
    elif abs_or_prp == "prp":
        return os.path.relpath(packageRootAbsPath, getPyprojectRootDir())
        


# EXAMPLES

# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/packages/util/src/cross_pipelines"
# package_root_path = getPackageRootPath(path, "abs")
# print(package_root_path)

# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/packages/dataManager/src"
# package_root_path = getPackageRootPath(path, "abs")
# print(package_root_path)


# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/packages/util/src/cross_pipelines"
# package_root_path = getPackageRootPath(path, "prp")
# print(package_root_path)

# path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/packages/dataManager/src"
# package_root_path = getPackageRootPath(path, "prp")
# print(package_root_path)