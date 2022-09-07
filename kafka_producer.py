from kafka import KafkaProducer
import base64

def image_producer():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    with open("./dogImages/test/002.Afghan_hound/Afghan_hound_00116.jpg", "rb") as imageFile:
        str1 = base64.b64encode(imageFile.read())
    
    producer.send('dogtopic', str1)


if __name__ == "__main__":
   image_producer()