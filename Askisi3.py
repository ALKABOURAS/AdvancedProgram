import json
import paho.mqtt.client as mqtt
from flask import Flask, request

app = Flask(__name__)

# MQTT broker settings
mqtt_broker = "localhost"
mqtt_port = 1313
mqtt_topic = "my_topic"

# Initialize MQTT client
mqtt_client = mqtt.Client()


@app.route("/publish", methods=["POST"])
def publish_message():
    # Get the text from the HTTP POST request
    text = request.data.decode("utf-8")

    # Publish the text to MQTT
    mqtt_client.publish(mqtt_topic, text)

    return "Message published to MQTT"


if __name__ == "__main__":
    # Connect to the MQTT broker
    mqtt_client.connect(mqtt_broker, mqtt_port)

    # Start the MQTT client loop in a separate thread
    mqtt_client.loop_start()

    # Run the Flask app
    app.run()
