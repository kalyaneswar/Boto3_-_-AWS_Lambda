# Import the boto3 library, which is the AWS SDK for Python
import boto3

# Create a high-level EC2 resource object (enables access to collections and attributes)
ec2 = boto3.resource('ec2')

# Iterate over all EC2 instances using the collection 'instances.all()'
for instance in ec2.instances.all():
    # Print the instance ID and instance type of each EC2 instance
    print(f"Instance id is {instance.instance_id} and instance type is {instance.instance_type}")
