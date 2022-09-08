from diagrams import Diagram, Cluster,Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import Client
from diagrams.custom import Custom
from diagrams.saas.chat import Slack
from diagrams.programming.language import Python

cluster_labels = {
    "fontcolor": "orange",
    "labeljust": "m"
}

with Diagram(
    name="Apache Kafka as a Streaming Platform",
    filename="./diagrams/outputs/kafkadiagram",
    direction="LR",
    outformat=["pdf" , "jpg"],
    curvestyle="curved",
    show=False,
):
    with Cluster("Compose Kafka", graph_attr=cluster_labels):
        docker = Custom("", "../resources/compose.png")
        kafka = Kafka("Confluent Platform")
    
    dogImg = Custom("Dog Image" , "../resources/dog.jpeg")
    producer = Custom("Producer", "../resources/cog.png")
    consumer = Client("Consumer")

    dogImg << Edge(color="black") << producer >> Edge(color="black") >> kafka << Edge(color="black") << consumer
    
    with Cluster("Compose Seldon", graph_attr=cluster_labels):
        docker = Custom("", "../resources/compose.png")
        seldon = Custom("Seldon-Core" ,  "../resources/seldon.png")
    consumer >> Edge(color="red", style="dashed") >> seldon << Edge(color="red", style="dashed") << consumer
    slack = Slack("Slack")
    consumer >> Edge(color="blue") >> slack