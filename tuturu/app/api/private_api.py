from fastapi import APIRouter, File, UploadFile, HTTPException
from ..services.image_servises import upload_image_to_minio, delete_image_from_minio

router = APIRouter()

@router.post("/images/upload", summary="Загрузить изображение в MinIO")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_url = await upload_image_to_minio(file)
        return {"image_url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/images/{image_name}", summary="Удалить изображение из MinIO")
async def delete_image(image_name: str):
    try:
        deleted = await delete_image_from_minio(image_name)
        if deleted:
            return {"message": f"Image {image_name} deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail=f"Image {image_name} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
