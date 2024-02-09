from google.cloud import bigquery
from termcolor import colored


def extract_table(client, dataset_id, table_id, project, bucket_name):
    try:
        destination_uri = f"gs://{bucket_name}/{table_id}.csv"
      
        dataset_ref = bigquery.DatasetReference(project, dataset_id)
        
        table_ref = dataset_ref.table(table_id)
        
        job_config = bigquery.job.ExtractJobConfig(destination_format="CSV")
        
        extract_job = client.extract_table(
            table_ref,
            destination_uri,
            location="US",  # Location must match that of the source table.
            #job_config=job_config,
        )
        
        extract_job.result()  # Waits for job to complete.
        
        return destination_uri
    except Exception as e:        
        print(colored(f"Error extracting table: {e}", "red")) # Red for warning
        
        raise e  # Return None to indicate an error