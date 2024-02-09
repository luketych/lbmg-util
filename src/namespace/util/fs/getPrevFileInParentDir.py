import os


""" Given the path to a file, return the path to the previous file in the same directory,
    sorted alphabetically. If the current file is the first file in the directory, return None.
    Filters out files starting with "x__" or "archive__", and hidden files.
"""
def getPrevFileInParentDir(currentFile, filter_out_prefixed=['.', 'x__', 'archive__']):
    # Get the directory of the current file
    fileDir = os.path.dirname(currentFile)
    
    # Get all sibling files in the directory
    siblingFiles = [f for f in os.listdir(fileDir) if os.path.isfile(os.path.join(fileDir, f))]

    # Filter out files based on the specified prefixes and hidden files
    filteredFiles = [f for f in siblingFiles if not any(f.startswith(prefix) for prefix in filter_out_prefixed)]

    # Sort the remaining files in alphabetical order
    sortedFiles = sorted(filteredFiles)

    # Find the index of the current file in the sorted list
    try:
        currentIndex = sortedFiles.index(os.path.basename(currentFile))
        
        # Check if there is a previous file
        if currentIndex > 0:
            # Return the path to the previous file
            prevFile = os.path.join(fileDir, sortedFiles[currentIndex - 1])
            return prevFile
        else:
            # No previous file found
            return None

    except ValueError:
        # Handle the case where the current file is not in the list
        print(f"Error: {currentFile} not found in the list of sibling files.")
        return None