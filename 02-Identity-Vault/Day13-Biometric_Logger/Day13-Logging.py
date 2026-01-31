import boto3
import time
import uuid

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('IdentityVaultLogs')

def lambda_handler(event, context):
    # Get bucket and file name from the S3 upload event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    try:
        # 1. Compare face in uploaded photo against a 'Source' photo 
        # (For this lab, we'll just detect faces to keep it simple)
        response = rekognition.detect_faces(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            Attributes=['ALL']
        )
        
        # 2. Determine Status
        status = "AUTHORIZED" if response['FaceDetails'] else "UNAUTHORIZED"
        
        # 3. Log to DynamoDB (Day 13 Task)
        table.put_item(
            Item={
                'AccessID': str(uuid.uuid4()),
                'Timestamp': str(int(time.time())), #set string in DynamoDB
                'Status': status,
                'FileName': key,
                'SecurityLevel': 'Level_1'
            }
        )
        print(f"Verification Complete: {status}")
        return {"Message": f"Verification Complete: {status}"}
        
    except Exception as e:
        print(e)
        raise e