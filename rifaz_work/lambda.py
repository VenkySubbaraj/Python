import boto3
import zipfile
import json

iam_client = boto3.client('iam')
policy_file_path = './s3_policy.json'
with open(policy_file_path, 'r') as policy_file:
    policy_document = json.load(policy_file)

{
    "Version": "2012-10-17",
    "Statement": [
        {
		    "Sid": "sample_testing",
            "Effect": "Allow",
            "Action": "lambda:*",
			"Resource": "*"
        }
    ]
}


policy_name = 's3_policy'
response = iam_client.create_policy(
    PolicyName=policy_name,
    PolicyDocument=json.dumps(policy_document)
)

policy_arn = response['Policy']['Arn']

role_name = 'testing_role'
role_file_path = './s3_role.json'
with open(role_file_path, 'r') as role_file:
    assume_role_policy_document = json.load(role_file)
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
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

lambda_client = boto3.client('lambda')
function_name = 'your-function-name'
zip_file_path = 'your-zip-file.zip'
handler_function = 'handler_function'
role_arn = 'role_arn'
with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
    # Add the files to the zip file
    zip_file.write('your_lambda_code.py')

lambda_client.create_function(
    FunctionName=function_name,
    Runtime='python3.8',
    Role=role_arn,
    Handler=f'{handler_function}.lambda_handler',
    Code={
        'ZipFile': open(zip_file_path, 'rb').read()
    },
    Timeout=15,  # Set the timeout for your Lambda function
    MemorySize=128  # Set the memory size for your Lambda function
)

print(f"Lambda function '{function_name}' created and code uploaded.")
