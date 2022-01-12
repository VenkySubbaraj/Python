import boto3
import socket
import os
import time
import subprocess

imageid = ["ami-0356b1cd4aa0ee970", "ami-057f7e34dc12e5ca5", "ami-055d15d9cfddf7bd3" ]
ec2 = boto3.resource('ec2', region_name='ap-southeast-1')
for Ids in imageid:
   instances=ec2.create_instances(
           ImageId=Ids,
           MinCount=1,
           MaxCount=1,
           InstanceType='t2.micro',
           KeyName='venkatesh',
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

time.sleep(90)
details = ec2.instances.all()
print(details)

for inst in details:
    if inst.public_ip_address != None:
        print(inst.public_ip_address)
        #time.sleep(20)
        user = ["ec2-user", "ubuntu"]
        for x in user:
            print(x)
            bashcommands = "ssh -i" + " " + './venkatesh.pem' + " "+ x +"@"+inst.public_ip_address + " " + "-y"
            print(bashcommands)
            output = os.system(bashcommands)
            print(output)
#       subprocess.run([ssh -i ./venkatesh.pem ]


