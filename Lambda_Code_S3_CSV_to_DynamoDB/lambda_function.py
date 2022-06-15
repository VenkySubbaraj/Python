import json
import boto3

client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('sales')

def lambda_handler(event, context):
    bucket_name= event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    response = client.get_object(Bucket=bucket_name, Key=file_name)
    data = response['Body'].read().decode('utf-8')
    emp_data = data.split("\n")
    replaced_item = [item.replace('\r',"")for item in emp_data]
    for single_data in replaced_item:
        removed_comma = single_data.split(",")
        table.put_item(
            Item = {
                "id": removed_comma[0],
                "Country": removed_comma[1]
            }
        )
