FROM ubuntu:20.04
WORKDIR /app
RUN apt-get update && apt-get install -y && apt-get install ffmpeg libsm6 libxext6  -y && apt-get clean
RUN apt-get -y install tesseract-ocr && apt-get install -y python3 python3-distutils python3-pip
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install  -r requirements.txt && rm -rf /root/.cache/pip
COPY . .