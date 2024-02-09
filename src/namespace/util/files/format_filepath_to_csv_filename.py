def format_filepath_to_csv_filename(filepath):
    # replace /'s with -'s to make a valid filename
    filename = filepath.replace('/', '-')
    
    filename = filename.replace('.py', '.csv')

    return filename