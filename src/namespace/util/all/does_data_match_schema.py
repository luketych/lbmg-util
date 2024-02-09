from .convert_row_list_into_their_types import convert_row_list_into_their_types
from namespace.util.csv import split_csv_row


'''
    1. Check to see if the column names match the schema
    2. Check to see if the data types match the schema
'''
def does_data_match_schema(data_str, schema):
  
    does_header_match = False
    
    data = data_str.split("\n")
    head = data[0]
    tail = data[1:]

    
    # 1. Check to see if the column names match the schema
    
    # Extract a list of names using a list comprehension
    schema_names_list = [d['name'] for d in schema]
    head_names_list = head.split(",")
    
    
    if schema_names_list == head_names_list:
        does_header_match = True
        
        
        
    # 2. Check to see if the data types match the schema
    
    schema_types_list = [d['type'] for d in schema]
    
    # Just look at the 1st row of data..
    
    first_row = tail[0]    
    first_row_list = split_csv_row(first_row) 
    first_row_datatypes = convert_row_list_into_their_types(first_row_list)
    
    
    if schema_types_list == first_row_datatypes:
        does_datatypes_match = True
    else:
        does_datatypes_match = False

    
    
    if does_header_match and does_datatypes_match:
        return True
    else:
        return False