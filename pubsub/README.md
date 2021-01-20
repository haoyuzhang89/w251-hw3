# Pub Sub Demo

This demo shows a basic publication subscription example.  You'll need to start by installing our MQTT client.
```
pip3 install paho-mqtt
```

These example require a MQTT broker to be running (see the mosquitto section).  They also read the env variable `MQTT` for the broker host.
You'll need two terminals, one for the server and one for the client.  In each, first export the MQTT variable with the hostname or IP Address of your broker.  For example:
```
export MQTT=localhost
```
Then in termainal one, run `python3 server.py` and in two, run `python3 client.py`

When the client app completes, you should see the following in the server's terminal:
```
Connected with result code 0
we have a message....
message received  Hello World
message topic= example
message qos= 0
message retain flag= 0
```
