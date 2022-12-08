import os
import base64
from celery import Celery
from PIL import Image
import cv2
import io
import numpy as np


app = Celery('tasks', broker=os.environ.get("CELERY_BROKER_URL"))


@app.task(name="start_img_preprocess")
def start_img_preprocess(img_str: str):

    imgdata = base64.b64decode(str(img_str))
    img = Image.open(io.BytesIO(imgdata))
    cv2_img = np.array(img)

    # convert img to grayscale
    gray_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    
    # apply thresholding
    bin_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    _, im_arr = cv2.imencode('.jpg', bin_img)
    im_bytes = im_arr.tobytes()
    jpg_as_str = base64.b64encode(im_bytes)

    return jpg_as_str.decode()