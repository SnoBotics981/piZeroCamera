# piZeroCamera
Code for image processing with a Raspberry Pi Zero and Raspberry Pi camera

Some documentation about the Raspberry Pi Camera can be found at:

https://www.raspberrypi.org/documentation/raspbian/applications/camera.md

Programs that are working

	captureImage.py:
		Originally set up as the initial experiments for using
		the Raspberry PI zero for astronomical applications.
		This is a good example of the different options there
		are. In it's current form the program will capture
		a set of images based on the input. The images are only
		stored a .jpg files and there is no display option
		available.

	continuousExample01.py:
		Using the picamera module to read 10 images and
		save them as image<number>.jpg. Not very useful
		but does have a code example of printing camera
		information.

	continuousExample02.py:
		Some addition features are display over the
		continuoueExample01.py. May be useful to see
		how resolution and framerate can be specified.

	raspberryPiCameraStillImagesStreamForProcessing.py:
		Grabbing a single image using the picamera module.
		The image is moved from the picamera to the Open CV
		module.

	raspberryPiCameraMovieExample01.py
		Grabbing a video stream. Currently hard coded to a framerate
		of 2 frames per second.

	webcam-cv2.py:
		Grabbing video feed using the Open CV module.


Python programs that are working - but not very well.

       basic3-ex13-lastSample.py
		This one is supposed to be showing on to setup a socket
		connection to recive images. It has lot of messages in
		red when I run the vlc and crashed after a few seconds.

	