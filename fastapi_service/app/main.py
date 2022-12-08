from fastapi import FastAPI
from routers.ocr import ocr


app = FastAPI()


app.include_router(ocr.router)


@app.get("/")
async def root():
    return {"message": "Hello Hackernoon.com!"}