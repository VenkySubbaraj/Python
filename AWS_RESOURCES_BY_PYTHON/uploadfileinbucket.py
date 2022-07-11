import boto3

venkat = boto3.client('s3', aws_access_key_id = input('aws_access_key_id') , aws_secret_access_key = input('aws_secret_key'), region_name = input ('region'))

with open('./Venkat.xls',"rb") as f:
    venkat.upload_fileobj(f, input("Bucket_name"), 'venkat')
