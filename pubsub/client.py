import paho.mqtt.client as mqtt #import the client1
import os


MQTT_BROKER = os.getenv('MQTT')

client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
client.publish("home/server","OFF")#publish

print("send done")