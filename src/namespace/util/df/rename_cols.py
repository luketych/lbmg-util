import pandas as pd


'''
EXAMPLE USAGE
df = pd.DataFrame({'date_day': [1, 2, 3], 'value': [4, 5, 6]})
df = rename_columns(df, [('date_day', 'date'), ('value', 'val')])
print(df)
'''
def rename_cols(data, names):
    """
    This function takes a list of data and a list of tuples as input.
    Each tuple contains the old column name and the new column name.
    It renames the columns and returns the updated data as a list of dictionaries.
    """
    # Convert data to DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])
    
    # Rename columns
    for old_name, new_name in names:
        if old_name in df.columns:
            df = df.rename(columns={old_name: new_name})

    # Convert DataFrame to list of dictionaries
    renamed_data = df.to_dict('records')

    
    return renamed_data