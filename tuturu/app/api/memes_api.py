from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from ..schemas.meme import Meme, MemeCreate, MemeUpdate
from ..services import meme_service
from ..core.db import get_db

router = APIRouter()

@router.get("/memes", response_model=list[Meme], summary="Получить список всех мемов с пагинацией")
async def read_memes(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    """
    Получить список всех мемов с пагинацией.

    :param skip: Количество записей для пропуска (пагинация)
    :param limit: Максимальное количество записей для возвращения (пагинация)
    :param db: Сессия базы данных

    :raises HTTPException 500: Ошибка сервера при запросе к базе данных
    """
    try:
        memes = await meme_service.get_memes(db, skip=skip, limit=limit)
        return memes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/memes/{id}", response_model=Meme, summary="Получить конкретный мем по его ID")
async def read_meme(id: int, db: AsyncSession = Depends(get_db)):
    """
    Получить конкретный мем по его ID.
    
    :param id: ID мема
    :param db: Сессия базы данных
    
    :raises HTTPException 404: Мем не найден
    :raises HTTPException 500: Ошибка сервера при запросе к базе данных
    """
    try:
        db_meme = await meme_service.get_meme(db, meme_id=id)
        if db_meme is None:
            raise HTTPException(status_code=404, detail="Meme not found")
        return db_meme
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/memes", response_model=Meme, summary="Добавить новый мем")
async def create_meme(meme: MemeCreate, db: AsyncSession = Depends(get_db)):
    """
    Добавить новый мем.
    
    :param meme: Данные нового мема
    :param db: Сессия базы данных
    
    :raises HTTPException 400: Дубликат мема
    :raises HTTPException 500: Ошибка сервера при запросе к базе данных
    """
    try:
        return await meme_service.create_meme(db=db, meme=meme)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Duplicated meme")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/memes/{id}", response_model=Meme, summary="Обновить существующий мем")
async def update_meme(id: int, meme: MemeUpdate, db: AsyncSession = Depends(get_db)):
    """
    Обновить существующий мем по его ID.
    
    :param id: ID мема для обновления
    :param meme: Новые данные мема
    :param db: Сессия базы данных
    
    :raises HTTPException 404: Мем не найден
    :raises HTTPException 400: Дубликат мема
    :raises HTTPException 500: Ошибка сервера при запросе к базе данных
    """
    try:
        db_meme = await meme_service.update_meme(db=db, meme_id=id, meme=meme)
        if db_meme is None:
            raise HTTPException(status_code=404, detail="Meme not found")
        return db_meme
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Duplicated meme")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/memes/{id}", response_model=Meme, summary="Удалить мем по его ID")
async def delete_meme(id: int, db: AsyncSession = Depends(get_db)):
    """
    Удалить мем по его ID.
    
    :param id: ID мема для удаления
    :param db: Сессия базы данных
    
    :raises HTTPException 404: Мем не найден
    :raises HTTPException 500: Ошибка сервера при запросе к базе данных
    """
    try:
        db_meme = await meme_service.delete_meme(db=db, meme_id=id)
        if db_meme is None:
            raise HTTPException(status_code=404, detail="Meme not found")
        return db_meme
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
