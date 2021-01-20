# FaceDetection

This example will use OpenCV to perform simple face detection on your NX.  You'll need to be able to display from the NX, e.g. VNC.

### Building Docker file
Clone this repository and change into the facedetection directory.  Note, this is assuming your id can invoke docker.  You may need to use sudo.

```
docker build -t facedemo .
```


### Running
Note, all scripts are using the device 0 for the camera and depneding on your configuration, you may need to update.
Start an instance.
```
docker run -ti --rm --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix facedemo bash
```
From the prompt, run `python3 haarcascade_cam.py`.


Press 'q' to stop while a window is focused to stop the program.
