from fastapi import APIRouter
from tasks import start_img_preprocess
from celery.result import AsyncResult
from .model import ImageBase64


router = APIRouter(
    prefix="/api/v1/img_prep",
    tags=["img_prep"],
)

@router.get("/status/{task_id}")
async def get_status(task_id):
    task_result = AsyncResult(task_id)
    return { "task_status": task_result.status }
    

@router.get("/img/{task_id}")
async def get_img(task_id):
    task_result = AsyncResult(task_id)
    return { "img": task_result.result }


@router.post("/img")
async def create_item(img: ImageBase64):
    task = start_img_preprocess.delay(img.img_body_base64)
    return { "task_id": task.id }