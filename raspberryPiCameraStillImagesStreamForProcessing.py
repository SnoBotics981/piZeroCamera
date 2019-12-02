# This example was grabbed from:
# https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

# import the necessary packages

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture

camera             = PiCamera()
camera.sensor_mode = 3
camera.resolution  = (640, 480)
rawCapture         = PiRGBArray(camera, size=(640, 480))

print 'camera.sensor_mode: ', camera.sensor_mode

# allow the camera to warmup
time.sleep(0.1)

while True:
        # grab an image from the Raspberry Pi camera

        # From the help page setting use_video_port to True
        # to grab images at a faster rate.
        
        camera.capture(rawCapture, format="bgr", use_video_port=True)
        image = rawCapture.array

	# show the frame
	cv2.imshow("Frame", image)
        
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

cv2.destroyAllWindows()


