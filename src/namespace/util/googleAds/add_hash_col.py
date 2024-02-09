def add_hash_col(data, date_col_name='date'):
    for row in data:
        row['hash'] = row['camp_id'] + "_" + row[date_col_name]
    
    # Reorder the columns to move 'hash' to the beginning
    reordered_data = [dict(hash=row.pop('hash', None), **row) for row in data]
    
    return reordered_data
