train:
	python3 train_model.py

kafka:
	curl --silent --output docker-compose.yml https://raw.githubusercontent.com/confluentinc/cp-all-in-one/7.2.1-post/cp-all-in-one/docker-compose.yml
	docker compose up -d
	
kafka-deploy:
	docker compose -f docker-compose-kafka.yaml up --build

requirements:
	pip install -r requirements.txt

mac:
	docker pull emacski/tensorflow-serving:latest-linux_arm64
	docker run -t --rm -p 8501:8501 --mount type=bind,source=/Users/endriveizaj/Documents/Test-Kafka/models/dog_model/,target=/models/dog_model/ -e MODEL_NAME=dog_model emacski/tensorflow-serving:latest-linux_arm64

	docker pull emacski/tensorflow-serving:latest-linux_arm64
	docker run -t --rm -p 8501:8501 --mount type=bind,source=/Users/endriveizaj/Documents/Test-Kafka/models/dog_model/,target=/models/dog_model/ -e MODEL_NAME=dog_model emacski/tensorflow-serving:latest-linux_arm64
