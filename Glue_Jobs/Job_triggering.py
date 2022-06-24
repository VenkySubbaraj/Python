from __future__ import print_function
import json
import boto3
import time
import sys
import time
from datetime import datetime

s3 = boto3.client('s3')
glue = boto3.client('glue')

def lambda_handler(event, context):
    gluejobname="s3_athlete_event_legacy"

    try:
        runId = glue.start_job_run(JobName=gluejobname)
        status = glue.get_job_run(JobName=gluejobname, RunId=runId['JobRunId'])
        print("Job Status : ", status['JobRun']['JobRunState'])
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist '
              'and your bucket is in the same region as this '
              'function.'.format(source_bucket, source_bucket))
    raise e
