def filter_for_cols(data, columns_to_keep):
    filtered_rows = []

    for row in data:
        # Create a new dictionary with only the columns to keep
        filtered_row = {col: row[col] for col in columns_to_keep if col in row}
        filtered_rows.append(filtered_row)
    
    return filtered_rows