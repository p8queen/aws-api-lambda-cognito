import boto3
from botocore.exceptions import BotoCoreError, ClientError
import os
import json
from dotenv import load_dotenv
load_dotenv()

# Replace the following variables with your Cognito details
USER_POOL_ID = os.getenv('USER_POOL_ID')
CLIENT_ID = os.getenv('CLIENT_ID')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
REGION_NAME = os.getenv('REGION_NAME')

# Initialize the Cognito client
client = boto3.client('cognito-idp', region_name=REGION_NAME)

# Authenticate the user

try:
    response = client.initiate_auth(
        ClientId=CLIENT_ID,
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': USERNAME,
            'PASSWORD': PASSWORD
        }
    )
    AccessToken = response['AuthenticationResult']['AccessToken']
    IdToken = response['AuthenticationResult']['IdToken']
    RefreshToken = response['AuthenticationResult']['RefreshToken']
    resBody = {'AccessToken':AccessToken,
                    'IdToken':IdToken,
                    'RefreshToken':RefreshToken
                    }
    with open('output_tokens.json', 'w') as f:
        f.write(json.dumps(resBody))
    print('Tokens written to output_tokens.txt')
except client.exceptions.NotAuthorizedException as e:
    resBody = {'Error':'User is not authorized'}
    print({'Error':'User is not authorized'})


