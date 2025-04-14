# Import the boto3 library, which is the AWS SDK for Python
import boto3

# Create a low-level service client for EC2
client = boto3.client('ec2')

# Launch a new EC2 instance using the specified AMI ID and instance type
# MaxCount and MinCount are set to 1, meaning a single instance will be launched
respone = client.run_instances(
    ImageId='ami-09c813fb71547fc4f',  # Specify the AMI ID to use
    InstanceType='t2.micro',          # Choose the instance type
    MaxCount=1,                       # Maximum number of instances to launch
    MinCount=1                        # Minimum number of instances to launch
)

# Iterate through the list of launched instances and print their Instance IDs
for instance in respone['Instances']:
    print(instance['InstanceId'])     # Output the Instance ID of each launched instance
