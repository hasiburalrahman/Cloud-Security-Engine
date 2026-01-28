import boto3
import json

# Initialize the Rekognition client
rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    # 1. Capture parameters from the Test Event
    action = event.get('action')
    bucket = event.get('bucket')
    photo = event.get('photo')
    name = event.get('name', 'Unknown_User')
    
    # Static Collection ID
    COLLECTION_ID = 'office-employees'

    try:
        # TASK 1: CREATE COLLECTION
        if action == 'create':
            try:
                rekognition.create_collection(CollectionId=COLLECTION_ID)
                return {"status": "Success", "msg": f"Collection '{COLLECTION_ID}' created."}
            except rekognition.exceptions.ResourceAlreadyExistsException:
                return {"status": "Success", "msg": "Collection already exists."}

        # TASK 2: INDEX (REGISTER) FACE
        elif action == 'index':
            response = rekognition.index_faces(
                CollectionId=COLLECTION_ID,
                Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
                ExternalImageId=name.replace(" ", "_"),
                DetectionAttributes=['ALL']
            )
            
            if not response['FaceRecords']:
                return {"status": "Error", "reason": "No face detected in the image."}
                
            face_id = response['FaceRecords'][0]['Face']['FaceId']
            return {
                "status": "Face Indexed",
                "FaceId": face_id,
                "Name": name
            }

        # TASK 3: SEARCH FOR MATCH
        elif action == 'search':
            response = rekognition.search_faces_by_image(
                CollectionId=COLLECTION_ID,
                Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
                MaxFaces=1,
                FaceMatchThreshold=70  # Forgiving threshold
            )
            
            # If the list of matches is empty
            if not response['FaceMatches']:
                return {
                    "status": "No Match Found", 
                    "reason": "The face in this photo does not match any authorized users."
                }
                
            # If a match is found
            match = response['FaceMatches'][0]
            return {
                "status": "MATCH CONFIRMED",
                "Identity": match['Face'].get('ExternalImageId', 'Unknown'),
                "Similarity": f"{match['Similarity']:.2f}%"
            }

        else:
            return {"status": "Error", "reason": "Invalid action. Use 'create', 'index', or 'search'."}

    except Exception as e:
        # Returns the exact error message (like the S3 Metadata error)
        return {"status": "Error", "reason": str(e)}