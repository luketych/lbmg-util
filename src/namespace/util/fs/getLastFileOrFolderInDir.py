import os


def getLastFileOrFolderInDir(directory, filter_out_prefixed=['.', 'x__', 'archive__']):
    # Get all files and folders in the directory
    entries = [entry for entry in os.listdir(directory) if os.path.exists(os.path.join(directory, entry))]

    # Filter out entries based on the specified prefixes and hidden files
    filtered_entries = [entry for entry in entries if not any(entry.startswith(prefix) for prefix in filter_out_prefixed)]

    # Sort the remaining entries in alphabetical order
    sorted_entries = sorted(filtered_entries)

    # Check if there are any entries after filtering
    if sorted_entries:
        # Return the path to the last entry
        last_entry = os.path.join(directory, sorted_entries[-1])
        return last_entry
    else:
        # No entries found after filtering
        return None