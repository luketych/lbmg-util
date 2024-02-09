from google.cloud import bigquery


def create_dataset(client, project, dataset_id):
    dataset = bigquery.Dataset(f"{project}.{dataset_id}")
    dataset.location = "US"
    dataset = client.create_dataset(dataset)
    print(f"Created BigQuery dataset: {project}.{dataset_id}")
    
    return dataset