# Import the boto3 library, which is the AWS SDK for Python
import boto3

# Create a low-level service client for EC2
client = boto3.client('ec2')

# Describe EC2 instances with a filter to list only running instances
response = client.describe_instances(Filters=[{
    'Name': 'instance-state-name',  # Filter by the instance state
    'Values': ['running']           # Only include instances that are currently running
}])

# Loop through the list of reservations returned by the describe_instances call
for Reservation in response['Reservations']:
    # Each reservation can contain multiple EC2 instances
    for instance in Reservation['Instances']:
        # Print the Instance ID of each running instance
        print(f"InstanceID is {instance['InstanceId']}")
