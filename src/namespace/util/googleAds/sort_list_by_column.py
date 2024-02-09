def sort_list_by_column(list_data, column_name, reverse=False):
    sorted_list = sorted(list_data, key=lambda x: x[column_name], reverse=reverse)
    return sorted_list