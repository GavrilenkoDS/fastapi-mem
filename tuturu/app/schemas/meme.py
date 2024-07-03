from pydantic import BaseModel

class MemeCreate(BaseModel):
    text: str
    image_url: str

class MemeUpdate(BaseModel):
    text: str

class Meme(BaseModel):
    id: int
    text: str
    image_url: str

    class Config:
        from_attributes = True

