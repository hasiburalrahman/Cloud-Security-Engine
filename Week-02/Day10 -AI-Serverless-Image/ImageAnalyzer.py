"""
ImageAnalyzer Lambda Function

Analyzes images uploaded to S3 using AWS Rekognition and stores results in DynamoDB.
Supports only standard image formats (JPG, JPEG, PNG).
"""

import boto3
import urllib.parse

# Initialize AWS service clients
rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageLabels')

def lambda_handler(event, context):
    """
    Main Lambda handler function.
    
    Args:
        event: S3 event containing bucket and object information
        context: Lambda context object
        
    Returns:
        dict: Status and results of image analysis
    """
    # Extract bucket and file name from S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    # Validate file format
    file_extension = key.split('.')[-1].lower()
    supported_formats = ['jpg', 'jpeg', 'png']
    
    if file_extension not in supported_formats:
        message = f"Skipping {key}: unsupported format '{file_extension}'"
        print(message)
        return {"status": "skipped", "reason": "unsupported format", "key": key}

    try:
        # Request label detection from Rekognition
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            MaxLabels=5,
            MinConfidence=50
        )

        # Extract label names from response
        labels = [label['Name'] for label in response['Labels']]
        
        # Store results in DynamoDB
        confidence = (
            str(response['Labels'][0]['Confidence']) 
            if labels 
            else "0"
        )
        
        table.put_item(
            Item={
                'ImageID': key,
                'Bucket': bucket,
                'Labels': labels,
                'Confidence': confidence
            }
        )
        
        return {
            "status": "success",
            "labels": labels,
            "key": key,
            "confidence": confidence
        }

    except Exception as e:
        print(f"Error processing {key}: {str(e)}")
        raise e