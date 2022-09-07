import logging
from kafka import KafkaConsumer
from base64 import decodebytes
from PIL import Image
import tensorflow as tf
import numpy as np
import json
import requests
import pickle
from slack_sdk import WebClient
from seldon_core.seldon_client import SeldonClient
import os

logging.basicConfig(level=logging.INFO)
config = os.getenv("CONFIG", "SELDON")

def send_photo_to_slack(result):
    image = open("foo.png", 'rb').read()
    client = WebClient("Slack_Bot_User_OAuth_Token") #input OAuth token
    client.files_upload(
        channels = "Slack_channel_id", #input channel id
        initial_comment = f"{result}",
        filename = "dog photo",
        content = image
    )

def send_client_request(seldon_client, image):
    client_prediction = seldon_client.predict(
        data=image,
        deployment_name="seldon-dogbreed",
        payload_type="ndarray"
    )
    return client_prediction



def predict_seldon(image):
    sc = SeldonClient(
        gateway="seldon",
        transport="rest",
        gateway_endpoint="localhost:9000"
    )
    prediction = send_client_request(sc, image)
    response = prediction.response.get("data").get("ndarray")
    pred = tf.argmax(response, axis=1)

    with open("./models/labels.pickle", "rb") as handle:
            idx_to_class1 = pickle.load(handle)
    idx_to_class = {value: key for key, value in idx_to_class1.items()}
    label = idx_to_class[pred.numpy()[0]]
    result = label.split(".")[-1].replace("_", " ")
    return result

def predict_tfserve(image):
    url = "http://localhost:8501/v1/models/dog_model:predict"
    data = json.dumps({ "signature_name": "serving_default","instances": image.tolist(),})
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    prediction = json.loads(response.text)["predictions"]
    pred = tf.argmax(prediction, axis=1)    

    with open("./models/labels.pickle", "rb") as handle:
        idx_to_class1 = pickle.load(handle)

    idx_to_class = {value: key for key, value in idx_to_class1.items()}
    label = idx_to_class[pred.numpy()[0]]
    result = label.split(".")[-1].replace("_", " ")
    return result


def consumer():
    consumer = KafkaConsumer('dogtopic')
    for message in consumer:
        with open("foo.png","wb") as f:
            f.write(decodebytes(message.value))
        img = tf.keras.utils.load_img(
            "foo.png",
            target_size=(224,224)
        )
        input_arr = tf.keras.utils.img_to_array(img)
        image = input_arr[None, ...]
        if config=="TENSORFLOW":
            print("Tensorflow")
            result = predict_tfserve(image)
        elif config=="SELDON":
            print("SELDON")
            result = predict_seldon(image)
        send_photo_to_slack(result)



if __name__ == "__main__":
    consumer()
