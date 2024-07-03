# Используем базовый образ Python
FROM python:3.9

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /tuturu



# Копируем все содержимое папки app в рабочую директорию контейнера
COPY ./app /tuturu/app

# Устанавливаем зависимости, например, через pip
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy aiofiles minio aiosqlite

# Определяем команду, которая будет запускаться при старте контейнера
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
