from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .api import memes_api, private_api
from .core.db import engine
from .models.meme import Base
from .core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Запуск")
    yield
    print("Остановка")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API для работы с коллекцией мемов и загрузки изображений",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/api/memes/docs",
    redoc_url="/api/memes/redoc",
    openapi_url="/api/memes/openapi.json"
)

origins = [
    "http://localhost",
    # Добавьте сюда другие разрешенные источники
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    memes_api.router,
    prefix="/api/memes",
    tags=["memes"]
)

app.include_router(
    private_api.router,
    prefix="/api/images",
    tags=["memes"]
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Meme API"}
