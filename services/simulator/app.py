import time
import json
import random
import pika
from datetime import datetime

# RabbitMQ connection    ONLY WORKS LOCALLY, for kubernates leeds to change
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')   # rabbitmq.messaging.svc.cluster.local
)

channel = connection.channel()
channel.queue_declare(queue='vehicle.location')

# starting position (example: Europe)
lat = 48.2082
lon = 16.3738

VIN = "D2S-001"

def simulate_movement():
    global lat, lon

    # small movement simulation
    lat += random.uniform(-0.0005, 0.0005)
    lon += random.uniform(-0.0005, 0.0005)

    return {
        "vin": VIN,
        "latitude": lat,
        "longitude": lon,
        "timestamp": datetime.utcnow().isoformat()
    }

while True:
    data = simulate_movement()

    channel.basic_publish(
        exchange='',
        routing_key='vehicle.location',
        body=json.dumps(data)
    )

    print("Sent:", data)

    time.sleep(2)