import boto3
import socket
import os
import time
import subprocess
import paramiko
from paramiko import BadAuthenticationType
from botocore.exceptions import ClientError


""" list the instance and delete the instance"""
import boto3

ec3_instance = boto3.client("ec2", region_name = "ap-southeast-1")
instances = ec3_instance.describe_instances(Filters=[
    {
        "Name": "instance-state-name",
        "Values": ["running"]
    }
    ])
#print(Reservations)
print(instances)

for inst in instances['Reservations']:
    for pythoninst in inst['Instances']:
        print(pythoninst['PublicDnsName'], pythoninst['InstanceType'], pythoninst['InstanceId'])
        ids = pythoninst['InstanceId']
        print(ids)
        ec2 = boto3.client("ec2", region_name = "ap-southeast-1")
        c = ec2.terminate_instances(InstanceIds=[ids])
        print(c)

time.sleep(80)
"""To list all the security group """
client = boto3.client('ec2')
output = client.describe_security_groups()
print(output)
reponse = client.delete_security_group( GroupName='Venkat_SG')
print(reponse)


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
           InstanceType='t2.xlarge',
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

time.sleep(120)
details = ec2.instances.all()
print(details)


""" details is a variable and assing to ec2.instances.all"""

for inst in details:
    if inst.public_ip_address != None:
        print(inst.public_ip_address)
        time.sleep(30)
        try:
            user = ["ec2-user", "ubuntu"]
            for x in user:
                print(x)
                if x:
                    if (x == "ec2-user"):
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        password = './sampledocker.pem'
                        print(password)
                        keypath = paramiko.RSAKey.from_private_key_file(password)
                        print(keypath)
                        print('inst.public_ip_address' + "public ip")
                        ssh.connect( inst.public_ip_address, username=x, pkey = keypath )
                        print("connectedi with ec2-user")
                    elif (x == "ubuntu"):
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        password = './sampledocker.pem'
                        print(password)
                        keypath = paramiko.RSAKey.from_private_key_file(password)
                        print(keypath)
                        print('inst.public_ip_address' + "public ip")
                        ssh.connect( inst.public_ip_address, username=x, pkey = keypath )
                        print("connectedi with ubuntu")
            
                else:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    password = './sampledocker.pem'
                    keypath = paramiko.RSAKey.from_private_key_file(password)
                    print(keypath)
                    print('inst.public_ip_address' + "public ip")
                    ssh.connect( inst.public_ip_address, username=x, pkey = keypath )
                    print("connected with ubuntu")

        except:
            print("Authentication Failure")

