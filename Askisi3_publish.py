import json
import paho.mqtt.client as mqtt

# MQTT broker settings
mqtt_broker = "broker.emqx.io"
mqtt_port = 1883
mqtt_topic = "python/mqtt"

# Initialize MQTT client
mqtt_client = mqtt.Client()

# Connect to the MQTT broker
mqtt_client.connect(mqtt_broker, mqtt_port)

# HTTP POST data
post_data = {
    "name": "John",
    "age": 25
}

# Convert HTTP POST request to a string
http_post_request = json.dumps(post_data)  # Convert to JSON string

# Publish the MQTT message with the HTTP POST request
mqtt_client.publish(mqtt_topic, http_post_request)

# Disconnect from the MQTT broker
mqtt_client.disconnect()
