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

	grabbingVideoStreamFromOrionTelescopeCamera.py:

		Hard coded to use usb 1. Nothing very special about
		this program.

	grabbingVideoStreamFromRaspberryPiCamera.py:

		Copied this code from the web site:
		https://gist.github.com/tedmiston/6060034
		The argument to the function show_webcam need to
		be set false to not mirror the image.
		Program is working correctly.

	grabbingVideoStreamFromUsbId.py:

		Takes as an argument the USB ID of the camera that
		will be streamed. For the Raspberry Pi Zero 0 is the
		Raspberry Pi Camera. 1 - N are actually USB cameras
		connected to the USB port(s).

		The original source of this program was the web side:
		https://gist.github.com/tedmiston/6060034

	raspberryPiCameraMovieExample01.py:

		This example was grabbed from:
		https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
		it worked to grab a video stream and display it
		When reduced to a 320x240 image at 16 frames per second I was
		seeing about a 1 second delay and about 80% of the CPU.
		As I'm running on a remote desktop some of the delay may in
		fact be due to trying to move the images from the Pi to my
		desktop computer
	
	raspberryPiCameraStillImagesStreamForProcessing.py:
	
		Grabbing a single image using the picamera module.
		The image is moved from the picamera to the Open CV
		module.

	raspberryPiCameraMovieExample01.py
	
		Grabbing a video stream. Currently hard coded to a framerate
		of 2 frames per second.

	raspberryPiCameraStillImagesStreamForProcessing.py:

		This example was grabbed from:
		https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
		Working to just grab a single image in a loop.
		
	webcam-cv2.py:
	
		Grabbing video feed using the Open CV module.

Shell Examples

      workingShellCommands.sh

		Examples of shell commands.

Python programs that are working - but not very well.

       basic3-ex13-lastSample.py
       
		This one is supposed to be showing on to setup a socket
		connection to recive images. It has lot of messages in
		red when I run the vlc and crashed after a few seconds.

	