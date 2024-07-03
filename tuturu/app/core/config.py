import os

class Settings:
    PROJECT_NAME: str = "Meme API"
    #DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+aiomysql://user:password@db/meme_db")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///game.db")
    MINIO_URL: str = os.getenv("MINIO_URL", "http://localhost:9000")
    MINIO_ACCESS_KEY: str = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
    MINIO_SECRET_KEY: str = os.getenv("MINIO_SECRET_KEY", "minioadmin")
    MINIO_BUCKET_NAME: str = os.getenv("MINIO_BUCKET_NAME", "memes")

settings = Settings()
