# NX and a sever



If you haven't been working on the NX, you'll need to check this repo and build the mosquitto image.  Once done, we'll be createing a docker network; this will allow us to `link` containers easier.

Run the command:
```
docker network create mqtt
```
This creates the network mqtt.  You can verify by running `docker network ls`.

In a terminal on the nx, start the broker with the command:
```
docker run -d --rm --name mqtt -p 1883:1883 --network mqtt mosquitto
```
Notice, we are using -d (detached).  You can see your container with the command `docker ps` and terminate it with `docker stop mqtt`.
