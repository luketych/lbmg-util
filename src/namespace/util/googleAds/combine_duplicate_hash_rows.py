''' Looks for rows with the same hash and combines some of the columns together.
'''
from datetime import datetime

def combine_duplicate_hash_rows(data, combine_columns, preserve_columns, date_format='%Y-%m-%d'):
    # Create a list to store combined data
    combined_data = []

    # Helper dict to find the hash in the combined_data list quickly
    hash_index_dict = {}

    for row in data:
        # Convert columns to appropriate data types, including dates
        for col_name, col_type in combine_columns:
            if col_name in row:
                if col_type == 'int':
                    if row[col_name] == '':
                      row[col_name] = 0
                    else:
                      row[col_name] = int(row[col_name])
                elif col_type == 'float':
                    if row[col_name] == '':
                      row[col_name]  = 0.0
                    else:
                      row[col_name] = float(row[col_name])
                elif col_type == 'date':
                    row[col_name] = datetime.strptime(row[col_name], date_format)

        hash_value = row['hash']

        if hash_value not in hash_index_dict:
            # Create a new dict for the combined_data list and store its index
            new_row = {col: row[col] for col in preserve_columns}
            for col_name, col_type in combine_columns:
                if col_name != 'date':
                    new_row[col_name] = row[col_name]
                else:
                    new_row[col_name] = [row[col_name]]

            combined_data.append(new_row)
            hash_index_dict[hash_value] = len(combined_data) - 1
        else:
            # Find the existing dict and update it
            existing_index = hash_index_dict[hash_value]
            combined_row = combined_data[existing_index]
            for col_name, col_type in combine_columns:
                if col_name == 'clicks':
                    combined_row[col_name] += row[col_name]
            combined_row['impressions'] += row['impressions']
            combined_row['spend'] += row['spend']
            combined_row['date'].append(row['date'])

    # Convert date lists to sorted strings
    for item in combined_data:
        item['dates'] = sorted([datetime.strftime(date, date_format) for date in item['date']], key=lambda x: x)
       
        # Remove the "date" column if it exists
        item.pop('date', None) 
        
        
    return combined_data