from googleapiclient import discovery
from google.oauth2 import service_account as sa
import os
import requests


def check_service_account_key(key_path):
    # Create a service account credentials object from the key file
    credentials = sa.Credentials.from_service_account_file(key_path)

    # Get the email of the service account associated with the key
    service_account_email = credentials.service_account_email

    # Check the permissions for the service account
    permission_request = requests.Request()
    iam_service = discovery.build('iam', 'v1', credentials=credentials)
    permissions_response = iam_service.projects().serviceAccounts().testIamPermissions(
        resource=f"projects/-/serviceAccounts/{service_account_email}",
        body={'permissions': ['*']}  # You can specify specific permissions instead of '*' if needed
    ).execute()

    # Get the service account details
    project_id = os.environ.get('GOOGLE_CLOUD_PROJECT')  # Assumes the project ID is set in the environment variable
    service_account_client = discovery.build('iam', 'v1', credentials=credentials)
    service_account = service_account_client.projects().serviceAccounts().get(
        name=f"projects/{project_id}/serviceAccounts/{service_account_email}"
    ).execute()

    # Print the permissions and service account details
    print(f"Permissions for Service Account {service_account_email}:")
    print(permissions_response.get('permissions'))
    print("\nService Account Details:")
    print(service_account)