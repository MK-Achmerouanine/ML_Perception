# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y python3-opencv tesseract-ocr libespeak1 ffmpeg espeak
RUN pip install -r requirements.txt
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
COPY . /code/
#ENV LISTEN_PORT=8080
#EXPOSE 8080
