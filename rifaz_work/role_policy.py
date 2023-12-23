import boto3
import json

json_file_path= './s3_policy.json'

iam_client = boto3.client('iam')
with open(json_file_path, 'r') as policy_file:
    policy_document = json.load(policy_file)
    print(policy_document)

policy_name = 's3_testin__policy'

response = iam_client.create_policy(
    PolicyName=policy_name,
    PolicyDocument=json.dumps(policy_document)
)

policy_arn = response['Policy']['Arn']

role_name = 'testing1_role'
role_file_path = './s3_role.json'
with open(role_file_path, 'r') as role_file:
    assume_role_policy_document = json.load(role_file)
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

role_response = iam_client.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(assume_role_policy_document)
)

role_arn = role_response['Role']['Arn']
iam_client.attach_role_policy(
    RoleName=role_name,
    PolicyArn=policy_arn
)

print(f"Role '{role_name}' created with ARN: {role_arn}")
print(f"Policy '{policy_name}' created with ARN: {policy_arn}")
