from .determine_data_type import determine_data_type


def convert_row_list_into_their_types(row_list):
    data_types = []
    
    for element in row_list:
        data_type = determine_data_type(element)
        data_types.append(data_type)
    
    return data_types