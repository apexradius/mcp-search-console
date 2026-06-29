import os

from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/webmasters"]


def get_service_account_credentials(credentials_file: str) -> service_account.Credentials:
    return service_account.Credentials.from_service_account_file(
        os.path.expanduser(credentials_file), scopes=SCOPES
    )
