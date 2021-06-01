FROM python:3.7-stretch as base

RUN mkdir -p /home/app

WORKDIR /home/app

COPY requirements.txt ./

RUN pip install -U py-mon
RUN pip install -r requirements.txt

COPY  . .

# Python app does not print anything when running detached in docker
ENV PYTHONUNBUFFERED="true"

ENV QUEUE_HOST=queue
ENV QUEUE_PORT=5672
ENV QUEUE_USERNAME=USER
ENV QUEUE_PASSWORD=PASSW
ENV RPC_QUEUE_NAME=RPC_QUEUE_NAME


FROM base as prod
CMD ["python" , "main.py"]


FROM base as dev

# nodemon for development purposes
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs
RUN npm i nodemon -g

CMD ["nodemon", "--legacy-watch", "--exec", "python" , "main.py"]