from json.tool import main
from traceback import print_tb
import boto3
import json

def create_role():
    client = boto3.client('iam', aws_access_key_id = 'AKIA4FZETVOEKYIJ3UNI', aws_secret_access_key = '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')
    try:
        print("INSIDE")
        my_managed_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect" : "Allow",
                    "Action": "logs:CreateLogGroup",
                    "Resource": "*"
                },
                {
                    "Effect" : "Allow",
                    "Action": [
                        "dynamodb:DeleteItem",
                        "dynamodb:GetIten",
                        "dynamodb:PutItem",
                        "dynamodb:Scan"
                    ],
                    "Resource": "*"
                }
            ]
        }
        print("insride2")

        response = client.create_policy(
            PolicyName = 'myDynamoDBPolicy_dup_one',
            PolicyDocument = json.dumps(my_managed_policy)
        )
        print(response)
    except:
        print("failed")
    return create_role

if __name__ == "__main__":
    create_role()