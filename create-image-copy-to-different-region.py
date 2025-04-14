import boto3

##########################
## Part-1: Create Images ##
##########################

source_region = 'ap-south-1'
ec2 = boto3.resource('ec2', region_name=source_region)

# Filter specific instances to create AMIs
instances = ec2.instances.filter(InstanceIds=['i-0067eeaab6c8188fd'])

image_ids = []

for instance in instances:
    # Create AMI from instance
    image = instance.create_image(
        Name='Demo-Boto-' + instance.id,
        Description='Demo Boto Image for ' + instance.id,
        NoReboot=True  # Optional: Avoid rebooting the instance
    )
    print(f"Creating image for instance {instance.id}: {image.id}")
    image_ids.append(image.id)

print("Images to be copied:", image_ids)


#############################################
## Part-2: Wait for Images to be available ##
#############################################

client = boto3.client('ec2', region_name=source_region)
waiter = client.get_waiter('image_available')

print("Waiting for images to become available...")
waiter.wait(Filters=[{
    'Name': 'image-id',
    'Values': image_ids
}])
print("Images are now available.")


##########################################
## Part-3: Copy Images to other region  ##
##########################################

destination_region = 'us-east-1'
client_dest = boto3.client('ec2', region_name=destination_region)

for image_id in image_ids:
    response = client_dest.copy_image(
        Name='Boto3 Copy - ' + image_id,
        SourceImageId=image_id,
        SourceRegion=source_region
    )
    print(f"Copied image {image_id} to {destination_region} as {response['ImageId']}")
