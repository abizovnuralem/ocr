from fastapi import FastAPI
from routers.tesseract import tesseract


app = FastAPI()


app.include_router(tesseract.router)


