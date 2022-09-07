# kafka-dogbreed-classification
Prerequisites:
* Docker
* Docker Compsoe
1. Set up the environment
    ```
    make requirements
    ```
2. Train dog model
    ```
    make train
    ```	
3. Download and start Confluent platform stack in detached mode
    ```
    make kafka
    ```
4. Run Seldon-Core and TensorFlow Serving
    ```
    make kafka-deploy
    ```
5. Run kafka consumer

    * #### TensorFlow Serving
        ```
        CONFIG=TENSORFLOW python kafka_consumer.py
        ```
    * #### Seldon-Core
        ```
        python kafka_consumer.py
        ```
6. Send image with kafka producer
    ```
    python kafka_producer.py
    ```
