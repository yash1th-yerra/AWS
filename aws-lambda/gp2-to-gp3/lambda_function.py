import json
import boto3


def extract_volume_id_from_arn(volume_arn):
    """Extracts the volume ID from the provided ARN."""
    # Split the ARN using colon ':' and fetch the volume ID
    volume_id = volume_arn.split(':')[-1].split('/')[-1]
    return volume_id


def lambda_handler(event, context):
    """Lambda function handler to convert EBS volumes to gp3 if they are of type gp2."""
    # Extract the volume ARN from the event
    volume_arn = event['resources'][0]
    volume_id = extract_volume_id_from_arn(volume_arn)
    
    # Create EC2 client
    ec2_client = boto3.client('ec2')
    
    # Fetch current volume details
    try:
        volume_details = ec2_client.describe_volumes(VolumeIds=[volume_id])
        current_volume = volume_details['Volumes'][0]
        
        # Check the current volume type
        if current_volume['VolumeType'] == 'gp2':
            # Modify the volume to gp3
            response = ec2_client.modify_volume(
                VolumeId=volume_id,
                VolumeType='gp3',
            )
            print(f"Volume {volume_id} successfully modified to gp3.")
        else:
            print(f"Volume {volume_id} is already {current_volume['VolumeType']}. No modification needed.")
    
    except Exception as e:
        # Log the error
        print(f"Error processing volume {volume_id}: {e}")
