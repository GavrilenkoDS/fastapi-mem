from minio import Minio

minio_client = Minio(
    "localhost:9000",
    access_key="your_username",
    secret_key="your_password",
    secure=False  # Используйте True, если MinIO настроен на использование HTTPS
)
