import requests
import boto3
import botocore
import json
import os
import sys


def get_secret(client, secret_name):
    response = client.get_secret_value(
        SecretId=secret_name
    )

    if 'SecretString' in response:
        secret_value = response['SecretString']
    else:
        # If the secret is stored as a binary value
        secret_value = response['SecretBinary']

    return secret_value

input_param=sys.argv[1]
secret_name_prefix = '<COMPANY-NAME>/<WORKSPACE-NAME>/<TEST-CASE-NAME>/'
secret_name=secret_name_prefix+input_param

# Create a session using the environment variables
session = boto3.Session()

secrets_manager_client = session.client(service_name='secretsmanager',region_name='cn-northwest-1')

retrieved_secret = get_secret(secrets_manager_client, secret_name)
print(retrieved_secret)
