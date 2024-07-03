from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models.meme import Meme
from ..schemas.meme import MemeCreate, MemeUpdate

async def get_memes(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Meme).offset(skip).limit(limit))
    return result.scalars().all()

async def get_meme(db: AsyncSession, meme_id: int):
    result = await db.execute(select(Meme).filter(Meme.id == meme_id))
    return result.scalar_one_or_none()

async def create_meme(db: AsyncSession, meme: MemeCreate):
    db_meme = Meme(**meme.dict())
    db.add(db_meme)
    await db.commit()
    await db.refresh(db_meme)
    return db_meme

async def update_meme(db: AsyncSession, meme_id: int, meme: MemeUpdate):
    result = await db.execute(select(Meme).filter(Meme.id == meme_id))
    db_meme = result.scalar_one_or_none()
    if db_meme:
        db_meme.text = meme.text
        await db.commit()
        await db.refresh(db_meme)
    return db_meme

async def delete_meme(db: AsyncSession, meme_id: int):
    result = await db.execute(select(Meme).filter(Meme.id == meme_id))
    db_meme = result.scalar_one_or_none()
    if db_meme:
        await db.delete(db_meme)
        await db.commit()
    return db_meme
