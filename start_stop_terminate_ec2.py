# Import the boto3 library, which is the AWS SDK for Python
import boto3

# Create a low-level service client for EC2
client = boto3.client('ec2')

# Attempt to start an EC2 instance
# client.start_instances(
#     InstanceIds=[
#         'i-092b57bb26f32e8a4',  # Specify the EC2 instance ID to start
#     ],
#     # AdditionalInfo parameter can be used to provide more info, optional
#     DryRun=True  # Set to True to check permissions without actually starting the instance
# )

# Attempt to stop the same EC2 instance
# client.stop_instances(
#     InstanceIds=[
#         'i-092b57bb26f32e8a4',  # Specify the EC2 instance ID to stop
#     ],
#     # AdditionalInfo parameter is optional
#     DryRun=True  # Set to True to simulate the stop action for permission check
# )

# Terminate the EC2 instance
response = client.terminate_instances(
    InstanceIds=[
        'i-092b57bb26f32e8a4',  # Specify the EC2 instance ID to terminate
    ],
    # AdditionalInfo is optional
    DryRun=False  # Set to False to actually terminate the instance
)

# Loop through the list of terminated instances and print their current state
for instance in response['TerminatingInstances']:
    print(instance["CurrentState"])  # Print the current state of the instance (e.g., shutting-down, terminated)
    print(f"The instance with ID {instance['InstanceId']} Terminated")  # Friendly message with instance ID
