import pika
import json
import os
from pymongo import MongoClient

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")

# MongoDB connection
client = MongoClient(f"mongodb://{MONGO_HOST}:27017/")
db = client["utracked"]
collection = db["locations"]

# RabbitMQ connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST)
)

channel = connection.channel()
channel.queue_declare(queue="vehicle.location")

def callback(ch, method, properties, body):
    data = json.loads(body)

    print("Received:", data)

    # store in MongoDB
    collection.insert_one(data)

channel.basic_consume(
    queue="vehicle.location",
    on_message_callback=callback,
    auto_ack=True
)

print("UTRACKED listening...")
channel.start_consuming()