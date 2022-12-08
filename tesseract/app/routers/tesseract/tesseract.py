from fastapi import APIRouter
from tasks import start_ocr_preprocess
from celery.result import AsyncResult
from .model import ImageBase64


router = APIRouter(
    prefix="/api/v1/tesseract",
    tags=["tesseract"],
)

@router.get("/status/{task_id}")
async def get_status(task_id):
    task_result = AsyncResult(task_id)
    return { "task_status": task_result.status }
    

@router.get("/text/{task_id}")
async def get_text(task_id):
    task_result = AsyncResult(task_id)
    return { "text": task_result.result }


@router.post("/img")
async def create_item(img: ImageBase64):
    task = start_ocr_preprocess.delay(img.img_body_base64)
    return { "task_id": task.id }