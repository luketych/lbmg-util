from .create_dataset import create_dataset


''' Create dataset if it doesn't exist and return it
    Otherwise, return the existing dataset
'''
def setup_dataset(client, project_id, dataset_id):
    try:
        dataset = client.get_dataset(f"{project_id}.{dataset_id}")
    except Exception as e:
        dataset = None
    
    if not dataset:
        dataset = create_dataset(client, project_id, dataset_id)
        
    return dataset