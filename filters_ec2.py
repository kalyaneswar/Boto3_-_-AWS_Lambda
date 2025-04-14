# Import the boto3 library, which is the AWS SDK for Python
import boto3

# Create a low-level service client for EC2
client = boto3.client('ec2')
response = client.describe_instances()

for Reservation in response['Reservations']:
    for instance in Reservation['Instances']:
        print(f"InstanceID is {instance['InstanceId']}")