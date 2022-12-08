from pydantic import BaseModel


class ImageBase64(BaseModel):
    img_body_base64: str


class PreProsImgResponse(BaseModel):
    task_id: str
