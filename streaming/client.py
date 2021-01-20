# Importing Libraries
import cv2 as cv
import paho.mqtt.client as mqtt
import base64
import time
import os

# get the brokers address/name
MQTT_BROKER = os.getenv('MQTT')
# Topic
MQTT_SEND = "streamingr"
# OpenCV time.  This is on device0
cap = cv.VideoCapture(0)
# Phao-MQTT Clinet
client = mqtt.Client()
# Connect
client.connect(MQTT_BROKER)
try:
 while True:
  start = time.time()
  # Read 
  _, frame = cap.read()
  # Encoding to jpeg
  _, buffer = cv.imencode('.jpg', frame)
  # this sends as text...
  jpg_as_text = base64.b64encode(buffer)
  # Publish
  client.publish(MQTT_SEND, jpg_as_text)
  end = time.time()
  t = end - start
  fps = 1/t
  print(fps)
except:
 cap.release()
 client.disconnect()
 print("\nAll Done...")
