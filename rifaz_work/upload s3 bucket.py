import boto3
s3_client = boto3.client('s3')
bucket_name = 'rifaz_bucket_testing_2023_12_22'
local_file_path = 'sample.txt'
s3_file_name = 'sample_s3_testing_file.txt'
s3_client.create_bucket(Bucket=bucket_name)
s3_client.upload_file(local_file_path, bucket_name, s3_file_name)

