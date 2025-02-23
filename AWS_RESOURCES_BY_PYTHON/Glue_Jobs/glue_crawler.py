
from __future__ import print_function
from distutils.cmd import Command
from sqlite3 import Connection
import boto3
import json
import time
import sys
import time
from datetime import datetime


client = boto3.client('glue', region_name="ap-south-1")
s3 = boto3.client('s3')

def s3_crawler_create() :
    response = client.create_crawler(
        Name='S3Crwaler',
        Role='arn:aws:iam::780467203909:role/service-role/AWSGlueServiceRole-SampleGlueJobs',
        DatabaseName='S3CrawlerHOC',
        Targets={
            'S3Targets': [
                {
                    'Path': 's3://mg-nab/Team3/',
                }
            ]
        },
        Schedule='',
        TablePrefix= '/',
        SchemaChangePolicy={
            'UpdateBehavior': 'LOG',
            'DeleteBehavior': 'LOG'
        },
        RecrawlPolicy={
            'RecrawlBehavior': 'CRAWL_EVERYTHING'
        },
        LineageConfiguration={
            'CrawlerLineageSettings': 'DISABLE'
        }
    )
    print(json.dumps(response, indent=4, sort_keys=True, default=str))

def Redshift_crawler_create() :
    response = client.create_crawler(
        Name='Redshift_Crawler',
        Role='arn:aws:iam::780467203909:role/service-role/AWSGlueServiceRole-SampleGlueJobs',
        DatabaseName='RedshiftCrawler',
        Targets={
            'JdbcTargets': [
                {
                    'ConnectionName': 'REDSHIFT_JDBC_CONNECTION',
                    'Path': 'dev/public/dockercontainer2',
                }
            ]
        },
        Schedule='',
        SchemaChangePolicy={
            'UpdateBehavior': 'LOG',
            'DeleteBehavior': 'LOG'
        },
        RecrawlPolicy={
            'RecrawlBehavior': 'CRAWL_EVERYTHING'
        },
        LineageConfiguration={
            'CrawlerLineageSettings': 'DISABLE'
        }
    )
    print(json.dumps(response, indent=4, sort_keys=True, default=str))


def glue_connection_create():
    response1 = client.create_connection(
        ConnectionInput={
            'Name': 'REDSHIFT_JDBC_CONNECTION',
            'ConnectionType': 'JDBC',
            'ConnectionProperties': {
                'JDBC_CONNECTION_URL': 'jdbc:redshift://redshift-cluster-2.cirefrc89xwr.ap-south-1.redshift.amazonaws.com:5439/dev',
                'USERNAME': '',
                'PASSWORD': ''
            },
            'PhysicalConnectionRequirements': {
                'SubnetId' : 'subnet-0e1db0fecd9cd4a8a',
                'SecurityGroupIdList': ['sg-0de8512432df6e091'],
                'AvailabilityZone': 'ap-south-1c'
            }
        }
    )
    print(response1)

def create_crawler_jobs():
    response =   client.create_job(
        Name = 'PARQUEET_JOBS',
        Role =  'arn:aws:iam::780467203909:role/service-role/AWSGlueServiceRole-SampleGlueJobs',
        ExecutionProperty = {
            'MaxConcurrentRuns':1
        },
        Command={
            'Name': 'python_code',
            'ScriptLocation': 's3://aws-glue-scripts-780467203909-ap-south-1/root/',
            'PythonVersion': '3'
        },
        Connections={
        'Connections': [
            'REDSHIFT_JDBC_CONNECTION',
            ]
        },
        GlueVersion='3.0',
        CodeGenConfigurationNodes={
            'string': {
                'S3ParquetSource': {
                    'Name': 'GlueJob',
                    'Paths': ['s3://dockercontainer1'],
                    'CompressionType': 'snappy',
                    'Recurse': True
                },
                # 'ApplyMapping': {
                #     'Name': 'S3_To_Parqueet',
                #     'Inputs': [
                #         'string',
                # ],
                # },
            #    'RedshiftTarget': {
            #         'Name': 'Redshift_gluejob',
            #         'Inputs': [
            #             'string'
            #         ],
            #         'Database': 'dev',
            #         'Table': 'dockercontainer2'
            #     },
            }
        }    
    )
    print(response)

def lambda_handler():
    gluejobname="PARQUEET_JOBS"

    try:
        runId = client.start_job_run(JobName=gluejobname)
        status = client.get_job_run(JobName=gluejobname, RunId=runId['JobRunId'])
        print("Job Status : ", status['JobRun']['JobRunState'])
        create_crawler_jobs()
        s3_crawler_create()
        Redshift_crawler_create()
        glue_connection_create()
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist '
              'and your bucket is in the same region as this '
              'function.'.format(source_bucket, source_bucket))
    print(e)

