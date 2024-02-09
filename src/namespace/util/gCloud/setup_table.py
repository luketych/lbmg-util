from .create_bigQuery_table import create_bigQuery_table


''' Create table if it doesn't exist, or if it exists but doesn't have the expected schema 
    and return it.
    Otherwise, return the existing table
'''
def setup_table(client, project_id, dataset, table_name, expected_schema):
    existing_schema = []
    should_create_new_table = False
    
    try:
        # check if table already exists with the same schema
        query_str = f"{project_id}.{dataset.dataset_id}.{table_name}"
        table = client.get_table(query_str) 
    except Exception as e:
        table = None
        
    if not table:
        should_create_new_table = True
        
    # if the table exists, check if it has the same schema
    elif table:
        table_schema = table.schema
        existing_schema = [field.to_api_repr() for field in table_schema]
        

        # if the schemas are different, create a new table
        if existing_schema != expected_schema:
            should_create_new_table = True
        else:
            should_create_new_table = False
    
    
    if should_create_new_table: 
        table = create_bigQuery_table(client, project_id, dataset.dataset_id, table_name, expected_schema, overwrite=True)
        
        
    return table