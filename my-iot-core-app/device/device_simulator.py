import paho.mqtt.client as mqtt
import json
import random
import time

# AWS IoT Core settings
AWS_IOT_ENDPOINT = "your-iot-endpoint.amazonaws.com"  # Replace with your AWS IoT endpoint
AWS_IOT_TOPIC = "traffic/simulator"

# Callback function for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

# Callback function for when a message is published
def on_publish(client, userdata, mid):
    print("Message published with mid: " + str(mid))

# Create an MQTT client
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to AWS IoT Core
client.connect(AWS_IOT_ENDPOINT, 8883, 60)

# Start the MQTT client loop
client.loop_start()

try:
    while True:
        # Simulate traffic intensity
        traffic_intensity = random.randint(0, 100)
        message = {
            "traffic_intensity": traffic_intensity
        }
        
        # Publish the message to the topic
        client.publish(AWS_IOT_TOPIC, json.dumps(message))
        print(f"Published message: {message} to topic: {AWS_IOT_TOPIC}")
        
        # Wait for a while before sending the next message
        time.sleep(5)

except KeyboardInterrupt:
    print("Device simulator stopped.")

finally:
    client.loop_stop()
    client.disconnect()