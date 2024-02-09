import os

from .download_blob import download_blob
from .extract_table import extract_table


def fetch_data(service_acct_key_path, client, dataset_id_with_table_id, project, bucket_name, destination_dir):
    dataset_id = dataset_id_with_table_id.split(".")[0]
    table_id = dataset_id_with_table_id.split(".")[1]
    
    source_blob_name = "{}.csv".format(table_id)
    destination_filepath = os.path.join(destination_dir, '{}.csv'.format(dataset_id + "." +table_id))
            
    destination_uri = extract_table(client, dataset_id, table_id, project, bucket_name)
    
    download_blob(service_acct_key_path, dataset_id, bucket_name, source_blob_name, destination_filepath)
    
    print( "Exported {}:{}.{} to {}".format(project, dataset_id, table_id, destination_uri) )