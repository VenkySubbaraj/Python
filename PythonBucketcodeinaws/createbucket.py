import boto3

s3_bucket = boto3.client('s3',aws_access_key_id=(input("aws_secret_key_id")),aws_secret_access_key=(input("aws_secret_key_token")),region_name=(input("region")))

s3create = s3_bucket.create_bucket(Bucket= (input("bucketname")), CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
