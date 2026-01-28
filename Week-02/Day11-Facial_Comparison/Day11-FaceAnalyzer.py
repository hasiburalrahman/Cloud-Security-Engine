import boto3
import json
import missing_module  # type: ignore

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    print(f"Executing function: {context.function_name}")
    print(f"Request ID: {context.aws_request_id}")
    
    # Check if we have enough time to run Rekognition
    if context.get_remaining_time_in_millis() < 1000:
         return {"error": "Not enough time to run AI comparison!"}
         
    # For this lab, we are hardcoding the bucket name for simplicity
    bucket = "identity-verification-lab-123" 
    source_photo = "Sirius_Black.jpeg"
    target_photo = "Jim Gordon.jpg"

    try:
        # The Face Comparison API
        response = rekognition.compare_faces(
            SourceImage={'S3Object': {'Bucket': bucket, 'Name': source_photo}},
            TargetImage={'S3Object': {'Bucket': bucket, 'Name': target_photo}},
            SimilarityThreshold=80 # We only care if it's 80% or higher
        )

        # Process the results
        if response['FaceMatches']:
            for match in response['FaceMatches']:
                similarity = match['Similarity']
                print(f"✅ Match Found! Similarity: {similarity:.2f}%")
                return {
                    "status": "Match",
                    "similarity": similarity
                }
        else:
            print("❌ No match detected.")
            return {"status": "No Match"}

    except Exception as e:
        print(f"Error: {e}")
        return {"status": "Error", "reason": str(e)}