import boto3
ec2 = boto3.resource('ec2')
instances=ec2.create_instances(
ImageId='ami-0d382e80be7ffdae5',
MinCount=1,
MaxCount=1,
InstanceType='t2.micro',
KeyName='DockerContainer'
)
