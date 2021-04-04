FROM python:3.7-stretch

RUN mkdir -p /home/app

WORKDIR /home/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY  . .

# Python app does not print anything when running detached in docker
ENV PYTHONUNBUFFERED="true"

ENV QUEUE_HOST=queue
ENV QUEUE_PORT=5672
ENV QUEUE_USERNAME=USER
ENV QUEUE_PASSWORD=PASSW
ENV RPC_QUEUE_NAME=RPC_QUEUE_NAME

CMD ["python" , "main.py"]
