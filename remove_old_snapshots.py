from datetime import datetime, timedelta, timezone
import boto3

# Create EC2 resource object
ec2 = boto3.resource('ec2')

# Get all snapshots owned by this account
snapshots = ec2.snapshots.filter(OwnerIds=['self'])

# Define the cutoff date: 15 days ago from current UTC time
delete_time = datetime.now(tz=timezone.utc) - timedelta(days=15)

# Iterate over each snapshot
for snapshot in snapshots:
    start_time = snapshot.start_time  # Timestamp when snapshot was created

    # Check if snapshot is older than 15 days
    if start_time < delete_time:
        # Delete the snapshot
        snapshot.delete()
        print(f"Snapshot with ID = {snapshot.snapshot_id} is deleted.")
