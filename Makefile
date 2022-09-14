train:
	docker build -t trainmodel:minikube --build-arg CONFIG="KUBERNETES" --file Dockerfile.train .
	docker run -t --rm -p 5002:5000  --mount type=bind,source=/Users/endriveizaj/Documents/kafka-dogbreed-classification/models,target=/models trainmodel:minikube

kafka:
	curl --silent --output docker-compose.yml https://raw.githubusercontent.com/confluentinc/cp-all-in-one/7.2.1-post/cp-all-in-one/docker-compose.yml
	docker compose up -d
	
kafka-deploy:
	docker compose -f docker-compose-kafka.yaml up --build

requirements:
	pip install -r requirements.txt