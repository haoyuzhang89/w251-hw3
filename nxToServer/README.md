# NX and a sever



If you haven't been working on the NX, you'll need to check this repo and build the mosquitto image.  Once done, we'll be createing a docker network; this will allow us to `link` containers easier.

Run the command:
```
docker network create mqtt
```
This creates the network mqtt.  You can verify by running `docker network ls`.

You'll want to recreate the mosquitto image on your NX.  See the mosquitto section for details.

In a terminal on the nx, start the broker with the command:
```
docker run -d --rm --name mqtt -p 1883:1883 --network mqtt mosquitto
```
Notice, we are using -d (detached).  You can see your container with the command `docker ps` and terminate it with `docker stop mqtt`.

We'll now creat an image for the NX that will send a message to our broker.  Change to the directory publishWithDocker and build the image:
```
docker build -t publishclient -f Dockerfile.client .
```
The Dockerfile uses Ubuntu in this example and installs a number of packages (python, pip, etc) along with our python packages 
```
FROM ubuntu
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt install -y python3-dev python3-pip vim-tiny
RUN pip3 install paho-mqtt
WORKDIR /apps
COPY client.py client.py
```
And our client.py
```
import paho.mqtt.client as mqtt #
import os


MQTT_BROKER = 'mqtt'

client = mqtt.Client("P1") 
client.connect(MQTT_BROKER) 
client.publish("example","Hello World")

print("send done")
```
Notice we are "hardcoding" the host name.  This is the same name we used when the broker was started.  When we run the container, we'll make sure to use the mqtt network, enabling us to use the container name as the hostname for lookups, making "linking" easier.

On your workstation, run the server.py from the pubsub example, using your NX's IP address as the value for the MQTT variable.  
Once the server is running, run the following on your nx:
```
docker run -it --rm --network mqtt publishclient bash
```
From the bash prompt, run `python3 client.py` and you should see the message show up on your workation.



Now we'll redo the streaming example.  Change to the directory `videoWithDocker`.  We'll build another image with the command:
``` 
docker build -t streamingclient -f Dockerfile.client .
```
As before, this will build our client image and install the needed packages and libraries.  Start the streaming server on your workstation, settig MQTT to the IP for your NX.  The client in this example also hardcodes the broker name, so will need to run it on the mqtt network.  In addition, we'll need to pass our video device, most likely video0.  
```
docker run -it --rm --network mqtt --device=/dev/video0 streamingclient bash
```
From the bash prompt, run `python3 client.py` and you should see the images from your NX's camera being displayed on your workstation!.
