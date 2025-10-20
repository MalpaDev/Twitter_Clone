"""
mqtt_handler.py
notes here
"""

import paho.mqtt.client as mqtt

class MQTTHandler:
    def __init__(self, broker="localhost", port=1883):
        self.client = mqtt.Client()
        self.broker = broker
        self.port = port


    def connect(self, on_message = None, on_connect = None):
        if on_message:
            self.client.on_message = on_message
        if on_connect:
            self.client.on_connect = on_connect

        print(f"Connecting to broker at {self.broker}:{self.port}")
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()
        print("Connected")

    def publish(self, topic, message):
        print(f"Publishing to topic {topic} : {message}")
        self.client.publish(topic, message)

    def subscribe(self, topic):
        print(f"Subscribing to topic {topic}")
        self.client.subscribe(topic)

    def unsubscribe(self, topic):
        print(f"unsubscribing from topic {topic}")
        self.client.unsubscribe(topic)

    def disconnect(self):
        print("Disconnecting")
        self.client.loop_stop()
        self.client.disconnect()
        print("Disconnected")
        