import boto3
import socket
import os
import time
import subprocess
import paramiko
from paramiko import BadAuthenticationType
from botocore.exceptions import ClientError

""" Creating the Security Group for the EC2 instance """
ec2 = boto3.client('ec2')

response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

print(vpc_id)
try:
    response = ec2.create_security_group(GroupName='Venkat_SG',
                                         Description='ManagedBy_Python',
                                         VpcId=vpc_id)
    security_group_id = response['GroupId']
    print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

    data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 80,
             'ToPort': 80,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ])
    #print('Ingress Successfully Set %s' % data)
except ClientError as e:
    print(e)


print(security_group_id)
imageid = ["ami-0356b1cd4aa0ee970", "ami-057f7e34dc12e5ca5", "ami-055d15d9cfddf7bd3" ]

""" Code to Create EC2_Instance"""

ec2 = boto3.resource('ec2', region_name='ap-southeast-1')
for Ids in imageid:
   instances=ec2.create_instances(
           ImageId=Ids,
           MinCount=1,
           MaxCount=1,
           InstanceType='t2.micro',
           KeyName='sampledocker',
           SecurityGroupIds= [ security_group_id ],

           TagSpecifications=[
              {
                   'ResourceType': 'instance',
                    'Tags': [
                        {
                           'Key': 'Name',
                           'Value': 'my-ec2-instance'
                           },
                        ]
                   },
               ]
           )

time.sleep(80)
details = ec2.instances.all()
print(details)

""" details is a variable and assing to ec2.instances.all"""

for inst in details:
    if inst.public_ip_address != None:
        print(inst.public_ip_address)
        time.sleep(5)
        try:
            user = ["ec2-user", "ubuntu"]
            for x in user:
                print(x)
                if x:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    password = './sampledocker.pem'
                    keypath = paramiko.RSAKey.from_private_key_file(password)
                    print(keypath)
                    print('inst.public_ip_address' + "public ip")
                    ssh.connect( inst.public_ip_address, username=x, pkey = keypath )
                    print("connected")
            #    print("This is a valid user")
                else:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    password = './sampledocker.pem'
                    keypath = paramiko.RSAKey.from_private_key_file(password)
                    print(keypath)
                    print('inst.public_ip_address' + "public ip")
                    ssh.connect( inst.public_ip_address, username=x, pkey = keypath )
                    print("connected")

        except:
            print("Authentication Failure")

