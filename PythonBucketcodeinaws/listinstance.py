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
