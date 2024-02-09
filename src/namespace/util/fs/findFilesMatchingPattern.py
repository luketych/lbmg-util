import os
import glob


"""
Find files in the specified base path matching the given pattern.

Parameters:
    base_path (str): The base directory to start searching.
    pattern (str): The pattern to match files.

Returns:
    list: A list of unique file paths that match the pattern.
"""
def findFilesMatchingPattern(path):

    file_paths = set()

    # Extract the last part of the path as the filename pattern
    pattern = os.path.basename(path)

    # Get the directory component from the path
    directory = os.path.dirname(path)

    # Construct the full directory path for globbing
    glob_directory = os.path.join(directory, '**')

    # Glob for files matching the pattern
    matching_files = glob.glob(os.path.join(glob_directory, pattern), recursive=True)

    # Filter out directories from the matching files
    matching_files = [file_path for file_path in matching_files if os.path.isfile(file_path)]

    file_paths.update(matching_files)

    return list(file_paths)



# Example usage
# path = '/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/data/system1/mirrored/segments/s0_fetchData/**/*daily*'

# matching_files = findFilesMatchingPattern(path)

# print("Matching Files:")
# for file_path in matching_files:
#     print(file_path)