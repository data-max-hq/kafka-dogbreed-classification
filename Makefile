train:
	python3 train_model.py

kafka:
	curl --silent --output docker-compose.yml https://raw.githubusercontent.com/confluentinc/cp-all-in-one/7.2.1-post/cp-all-in-one/docker-compose.yml
	docker compose up -d
	
kafka-deploy:
	docker compose -f docker-compose-kafka.yaml up --build

requirements:
	pip install -r requirements.txt