import os
import time
import base64
import pytesseract
from celery import Celery


app = Celery('tasks', broker=os.environ.get("CELERY_BROKER_URL"))


@app.task(name="start_ocr_preprocess")
def start_ocr_preprocess(img: str):
    with open("img.jpg",'wb') as f:
        f.write(base64.b64decode(img))
    text = pytesseract.image_to_string("img.jpg")
    time.sleep(30)
    os.remove("img.jpg")
    return text