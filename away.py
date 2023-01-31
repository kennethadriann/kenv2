import sys
import logging
import os
import json
import time

import msal

# Define your tenant ID and client ID
TENANT_ID = "your_tenant_id"
CLIENT_ID = "your_client_id"

# Define the authority and scopes
AUTHORITY = "https://login.microsoftonline.com/{}".format(TENANT_ID)
SCOPES = ["https://graph.microsoft.com/.default"]

# Create a callback to handle the redirect from Azure AD
def acquire_token_callback(authority, scopes, username, password, client_id, client_credential, redirect_uri):
    # Create the MSAL client
    app = msal.PublicClientApplication(client_id, authority=authority)

    # Acquire a token for the user
    result = None
    result = app.acquire_token_by_username_password(
        username=username,
        password=password,
        scopes=scopes
    )

    # Check the result
    if "access_token" in result:
        print("Access token: ", result["access_token"])
    else:
        print("Error acquiring access token: ", result.get("error"))
        print("Error description: ", result.get("error_description"))
        print("Correlation ID: ", result.get("correlation_id"))

# Main function
def main():
    # Get the username and password from environment variables
    username = os.environ["AZURE_AD_USERNAME"]
    password = os.environ["AZURE_AD_PASSWORD"]

    # Call the function to acquire a token
    acquire_token_callback(AUTHORITY, SCOPES, username, password, CLIENT_ID, None, None)

# Call the main function
if __name__ == "__main__":
    main()
