from google.cloud import storage
from termcolor import colored


def download_blob(service_acct_key_path, dataset_id, bucket_name, source_blob_name, destination_filename):
    '''Downloads a blob from the bucket'''
    
    try:
        # storage_client = storage.Client()
        storage_client = storage.Client.from_service_account_json(service_acct_key_path)


        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)

        blob.download_to_filename(destination_filename)

        print(
            "Downloaded storage object {} from bucket {} to local file {}.".format(
                source_blob_name, bucket_name, destination_filename
            )
        )
    except Exception as e:        
        print(colored(f"Error downloading blob: {e}", "red"))
        
        raise e