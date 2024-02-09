from google.cloud import bigquery

def load_client(key_path):
    try:
        #client = bigquery.Client()
        client = bigquery.Client.from_service_account_json(key_path)
        #client = service_account.Credentials.from_service_account_file(key_path)
        
        return client
    except Exception as e:
        print(f"Error loading client: {e}")
        return None  # Return None to indicate an error