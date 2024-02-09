from google.cloud import bigquery


def create_bigQuery_table(client, project, dataset_id, table_id, schema, overwrite=False):
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    
    table = bigquery.Table(table_ref, schema=schema)
    
    try:
        client.create_table(table)
        print(f"Created BigQuery table: {project}:{dataset_id}.{table_id}")
    except Exception as e:
        print(f"Error creating BigQuery table: {e}")
        
        if overwrite:
            print(f"Overwriting BigQuery table: {project}:{dataset_id}.{table_id}")
            
            client.delete_table(table_ref)
            table = client.create_table(table)
            
            
    return table