from django.db import models
import boto3

class MediaFile(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="uploads/")
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_presigned_url(self):
        s3 = boto3.client("s3", region_name="us-east-1")
        return s3.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": "adhish-march-media-2026",
                "Key": file_key,
            },
            ExpiresIn=300,
        )