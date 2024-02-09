from google.cloud import bigquery


def upload_data_to_bigQuery(client, dataset_id, table_id, source_file):
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    
    # Load the data from a local CSV file to BigQuery
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,  # Skip CSV header row
        autodetect=True,  # Detect schema automatically
    )

    try:
        with open(source_file, "rb") as source_file:
            job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
        
        job.result()  # Waits for job to complete
        
        print(f"Uploaded data to BigQuery: {dataset_id}.{table_id}")
    except Exception as e:
        print(f"Error uploading data to BigQuery: {e}")