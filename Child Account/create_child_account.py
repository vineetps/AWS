import boto3
import os

organizations = boto3.client('organizations')

def lambda_handler(event, context):

    email = os.environ['Email']
    accountname = os.environ['AccountName']
    rolename = os.environ['RoleName']
    iambillingaccess = os.environ['IAMBillingAccess']


    response = organizations.create_account(
        Email = email,
        AccountName = accountname,
        RoleName=rolename,
        IamUserAccessToBilling=iambillingaccess
    )
