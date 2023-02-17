import gzip
import io
import sys
import boto3
import subprocecss
from zipfile import ZipFile
import zipfile
from io import BytesIO
from awsglue.utils import getResolvedOptions
import tarfile

def unzip_file(bucket_name, config_key):
    s3 = boto3.clinet('s3')
    prefix = "adobe_file/"
    
    zipped_keys = s3.list_objects_V2(Bucket=bucket_name, Prefix=prefix, Delimeter="adobe_file/")
    file_list = []
    for key in zipped_keys['Contents']:
        file_list.append(key['Key'])
        print(file_list)
    
    for key_value_list in file_list[1:]:
        print(key_value_list)
        compressed_file = s3.get_object(Bucket=bucket_name, Key=key_value_list)['Body'].read()
        print(compressed_file)
        file_renamed = key_value_list.replace('.gz','')
        s3.put_object(Bucket=bucket_name, Key=file_renamed, Body=compressed_file)

def main ():
    args=getResolvedoptions(sys.argv, ['job_name', 'bucket', 'key'])
    bucket_name = args['bucket']
    config_key = args['key']
    job_name = args['job_name']
    unzip_file(bucket_name, config_key)

if __name__ == "__main__" :
    main()
    
