FROM python:3.8


RUN apt-get update && DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y curl python3-setuptools && \
    apt-get clean && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

RUN mkdir /models

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt 

COPY /apps .

ENV MODEL_NAME DogBreed
ENV SERVICE_TYPE MODEL

EXPOSE 9000

RUN chown -R 8888 /app
CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE 