import json
from datetime import datetime
import boto3
from botocore.exceptions import BotoCoreError, ClientError

from .config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    S3_BUCKET_NAME,
)

def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION,
    )

def upload_weather_data(data: list):
    """
    Upload weather data list to S3 as a JSON file.
    File name includes timestamp for historical tracking.
    """
    s3 = get_s3_client()
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    key = f"weather_data/weather_{timestamp}.json"

    try:
        body = json.dumps(data, indent=2)
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=key,
            Body=body.encode("utf-8"),
            ContentType="application/json",
        )
        print(f"[INFO] Uploaded weather data to s3://{S3_BUCKET_NAME}/{key}")
    except (BotoCoreError, ClientError) as e:
        print(f"[ERROR] Failed to upload to S3: {e}")

