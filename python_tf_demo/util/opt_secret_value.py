import requests
import boto3
import botocore
import json
import os

def create_secret(client, secret_name, secret_value):
    try:
        response = client.create_secret(
            Name=secret_name,
            SecretString=secret_value
        )
        return response
    except botocore.exceptions.ClientError as error:
       error_code = error.response['Error']['Code']
       error_message = error.response['Error']['Message']
       print(f"Error creating secret: {error_code} - {error_message}")
       return None

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

# AWS Secrets Manager
secret_name_prefix = '<COMPANY-NAME>/<WORKSPACE-NAME>/<TEST-CASE-NAME>/'

# Retrieve AWS credentials from system environment variables
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
aws_region = os.environ.get('AWS_REGION')

# Create a session using the environment variables
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

secrets_manager_client = session.client('secretsmanager')

secret_name=secret_name_prefix + '<YOUR-SECRET-NAME>'
secret_value='<YOUR-SECRET-VALUE>'
create_secret(secrets_manager_client, secret_name, secret_value)
