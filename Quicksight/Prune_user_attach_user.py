import boto3
from datetime import datetime, timedelta

# AWS credentials and region
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'us-west-2'

# QuickSight client
quicksight_client = boto3.client('quicksight', region_name=region_name,
                                 aws_access_key_id=aws_access_key_id,
                                 aws_secret_access_key=aws_secret_access_key)

# Prune QuickSight users who haven't logged in for 60 days
def prune_inactive_users(days_threshold):
    now = datetime.utcnow()
    inactive_users = []

    response = quicksight_client.list_users()
    users = response['UserList']

    for user in users:
        last_seen_time = user.get('LastSeen', None)

        if last_seen_time:
            last_seen_time = datetime.strptime(last_seen_time, '%Y-%m-%d %H:%M:%S.%f')

            if now - last_seen_time > timedelta(days=days_threshold):
                inactive_users.append(user['UserName'])

    if inactive_users:
        for user in inactive_users:
            response = quicksight_client.delete_user(
                UserName=user,
                AwsAccountId='YOUR_AWS_ACCOUNT_ID',
                Namespace='default'
            )
            print(f"Deleted user: {user}")

    else:
        print("No inactive users found.")

# Add a new user to a QuickSight group when assigned a specific role
def add_user_to_group(username, groupname, rolename):
    response = quicksight_client.create_user(
        AwsAccountId='YOUR_AWS_ACCOUNT_ID',
        Namespace='default',
        IdentityType='QUICKSIGHT',
        UserRole=rolename,
        UserName=username
    )

    user_arn = response['User']['Arn']

    response = quicksight_client.create_group_membership(
        AwsAccountId='YOUR_AWS_ACCOUNT_ID',
        Namespace='default',
        GroupName=groupname,
        MemberName=user_arn
    )

    print(f"Added user {username} to group {groupname} with role {rolename}")

# Usage example
prune_inactive_users(days_threshold=60)
add_user_to_group('new_user@example.com', 'group_name', 'role_name')
