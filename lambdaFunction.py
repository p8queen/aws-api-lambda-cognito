import json
import os
import boto3
from botocore.exceptions import BotoCoreError, ClientError

def lambda_handler(event, context):
    # TODO implement
    POOL_ID = os.environ['USER_POOL_ID']
    CLIENT_ID = os.environ['CLIENT_ID']
    REGION_NAME = os.environ['REGION_NAME']
    USERNAME = event['username']
    PASSWORD = event['password']
    
    # Initialize the Cognito client
    client = boto3.client('cognito-idp', region_name=REGION_NAME)
    
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
    except client.exceptions.NotAuthorizedException as e:
        resBody = {'Error':'User is not authorized'}

    return {
        'statusCode': 200,
        'body': resBody
    }
