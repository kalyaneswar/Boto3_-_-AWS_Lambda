import boto3

# Create EC2 resource and SNS client
ec2 = boto3.resource('ec2')
sns_client = boto3.client('sns')

# Filter to get EC2 instances with the tag Backup=Yes
backup_filter = [
    {
        'Name': 'tag:Backup',
        'Values': ['Yes']
    }
]

# Initialize lists
snapshot_ids = []
instances_skipped = []

# Filter EC2 instances that require backup
for instance in ec2.instances.filter(Filters=backup_filter):
    
    # Get all volumes attached to the instance
    volumes = list(instance.volumes.all())

    if volumes:
        for vol in volumes:
            # Create snapshot for each volume
            snapshot = vol.create_snapshot(Description='Created by Boto3')
            snapshot_ids.append(snapshot.snapshot_id)
    else:
        # No volumes attached — nothing to back up
        instances_skipped.append(instance.instance_id)

# Compose message for SNS
message_body = f"EBS Snapshots Created: {snapshot_ids}\n\n"
if instances_skipped:
    message_body += f"No volumes found to backup for instances: {instances_skipped}"

# Publish message to SNS
sns_client.publish(
    TopicArn='arn:aws:sns:us-east-1:992382707826:Snapshots',
    Message=message_body,
    Subject='EBS Snapshot Report',
)
