from fastapi import FastAPI, UploadFile, File
import boto3
import uuid
from config import S3_BUCKET, S3_FOLDER, AWS_REGION
app = FastAPI()



# Boto3 client
s3_client = boto3.client("s3", region_name=AWS_REGION)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Generate random image name
        file_extension = file.filename.split(".")[-1]
        image_key = f"{S3_FOLDER}{uuid.uuid4()}.{file_extension}"

        # Read file bytes
        file_bytes = await file.read()

        # Upload to S3
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=image_key,
            Body=file_bytes,
            ContentType=file.content_type,   # Correct Content-Type (important)
            ACL="public-read"                # Optional → makes it viewable in browser
        )

        public_url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{image_key}"

        return {
            "message": "Image uploaded successfully!",
            "image_url": public_url
        }

    except Exception as e:
        return {"error": str(e)}
