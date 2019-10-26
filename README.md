# piZeroCamera
Code for image processing with a Raspberry Pi Zero and Raspberry Pi camera

Some documentation about the Raspberry Pi Camera can be found at:

https://www.raspberrypi.org/documentation/raspbian/applications/camera.md

Programs that were working

webcam-cv2.py:
	Grabbing video feed using the Open CV module.

raspberryPiCameraStillImagesStreamForProcessing.py:
	Grabbing a single image using the picamera module.
	The image is moved from the picamera to the Open CV
	module.

raspberryPiCameraMovieExample01.py
	Grabbing a video stream. Currently hard coded to a framerate
	of 2 frames per second.
	