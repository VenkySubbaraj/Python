import boto3
from datetime import datetime, timedelta

def list_users(iam_client):
    response = iam_client.list_users()
    return response['Users']

def list_access_keys(iam_client, username):
    response = iam_client.list_access_keys(UserName=username)
    return response['AccessKeyMetadata']

def rotate_access_key(iam_client, username, access_key_id):
    iam_client.update_access_key(
        UserName=username,
        AccessKeyId=access_key_id,
        Status='Inactive'
    )
    new_key_response = iam_client.create_access_key(UserName=username)
    return new_key_response['AccessKey']

def check_and_rotate_keys(iam_client, max_age_days=90):
    users = list_users(iam_client)

    for user in users:
        username = user['UserName']
        access_keys = list_access_keys(iam_client, username)

        for key in access_keys:
            key_id = key['AccessKeyId']
            create_date = key['CreateDate']
            age = (datetime.now() - create_date).days

            if age > max_age_days:
                print(f"Rotating access key for user '{username}', key ID: {key_id}, age: {age} days.")
                new_key = rotate_access_key(iam_client, username, key_id)
                print(f"New access key generated: {new_key['AccessKeyId']}")

def main():
    # Specify your AWS region
    aws_region = 'your_aws_region'

    # Create IAM client
    iam_client = boto3.client('iam', region_name=aws_region)

    # Check and rotate access keys
    check_and_rotate_keys(iam_client)

if __name__ == "__main__":
    main()
