from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from ..core.config import POSTGRES_DSN_ASYNC


DATABASE_URL = POSTGRES_DSN_ASYNC

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():    
    async with AsyncSessionLocal() as session:
        yield session