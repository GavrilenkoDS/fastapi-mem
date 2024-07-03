from minio.error import S3Error
from fastapi import UploadFile

from ..core.storage import minio_client

async def upload_image_to_minio(file: UploadFile, bucket_name: str = "images") -> str:
    try:
        found = minio_client.bucket_exists(bucket_name)
        if not found:
            minio_client.make_bucket(bucket_name)

        file_name = file.filename
        file_data = await file.read()
        file_size = len(file_data)
        content_type = file.content_type

        response = minio_client.put_object(
            bucket_name,
            file_name,
            file_data,
            file_size,
            content_type=content_type
        )

        return minio_client.presigned_get_object(bucket_name, file_name)
    
    except S3Error as err:
        raise Exception(f"MinIO error occurred: {err}")

async def delete_image_from_minio(image_name: str, bucket_name: str = "images") -> bool:
    try:
        minio_client.remove_object(bucket_name, image_name)
        return True
    except S3Error as err:
        raise Exception(f"MinIO error occurred: {err}")
