import csv
from distutils.log import error
from http import client
from venv import create
import pandas as pd
import petl as etl
import psycopg2
from sqlalchemy import *
import boto3

redshift_endpoint = input('redshift_endpoint')
username= input('username')
password=input('password')
port=5439
database_name=input('database_name')
sql_query = """SELECT * FROM "dev"."public"."sample";"""
# sql_query = """CREATE TABLE "public"."sample"(dateid  smallint NOT NULL,
#                              caldate date NOT NULL encode az64,
#                              day     character(3) NOT NULL encode lzo,
#                              week    smallint NOT NULL encode az64,
#                              month   character(5) NOT NULL encode lzo,
#                              qtr     character(5) NOT NULL encode lzo,
#                              year    smallint NOT NULL encode az64,
#                              holiday boolean)distkey(dateid) compound sortkey(dateid);"""

def connection_path():
    try:
        engine="postgresql+psycopg2://%s:%s@%s:%d/%s" % (username, password, redshift_endpoint, port, database_name)
        print(engine)
        engine_con = create_engine(engine)
        print(engine_con)
        df1 =pd.read_sql_query(sql_query, engine_con)
        print(df1)
        df1.to_csv('./data.csv')
    except Exception as error:
        print(error)

def placing_file_in_bucket():
    try:
        s3_object = boto3.client('s3', aws_access_key_id=input('Access_key_ID'), aws_secret_access_key=input('Access_key_ID'), region_name='ap-south-1')
        with open('./data.csv', 'rb') as data:
            response=s3_object.put_object(Body=data,Bucket='testing56s',Key='data.csv')
            print(response)
    except Exception as error:
        print(error)

if __name__=="__main__":
    connection_path()
    placing_file_in_bucket()