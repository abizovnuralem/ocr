from fastapi import FastAPI
from routers.img_prepro import img_prepro


app = FastAPI()


app.include_router(img_prepro.router)


