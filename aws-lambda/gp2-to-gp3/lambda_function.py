import json
import boto3 


def extract_volume_id_from_arn(volume_arn):
    # split the arn using colon ':'
    arn_parts = volume_arn.split(':')
    # volume id is last part of the arn after volume/
    # arn:aws:ec2:ap-south-1:651706748444:volume/vol-03b03d567e518bac9
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id


def lambda_handler(event, context):
    # TODO implement
    # event is cloudwatch event since cloudwatch is invoking this lambda function
    
    # In event we are having ec2 resources
    volume_arn = event['resources'][0]
    volume_id = extract_volume_id_from_arn(volume_arn)
    ec2_client = boto3.client('ec2')
    response = ec2_client.modify_volume(
        VolumeId=volume_id,
        VolumeType='gp3',
    )