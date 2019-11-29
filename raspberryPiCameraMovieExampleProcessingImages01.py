# This example was grabbed from:
# https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
# it worked to grab a video stream and display it
# When reduced to a 320x240 image at 16 frames per second I was seeing
# about a 1 second delay and about 80% of the CPU.
# As I'm running on a remote desktop some of the delay may in fact
# be due to trying to move the images from the Pi to my desktop computer

# 2019-11-29 Code modified to accept as it's first argument the rotation
# angle. This much be 0, 90, 180, or 270. As it turns out -90 gets converted
# by the PiCamera class to a 270. There are currently not checks for the
# input value. This needs to be added.

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import sys
import cv2

def processAndDisplayImage (rotationAngle = 0):

    print 'rotationAngle: ', rotationAngle
    
    # original code was using a 640 x 480 image and had
    # about 1-2 seconds of delay.

    # initialize the camera and grab a reference to the raw camera capture
    camera            = PiCamera()
    camera.resolution = (640, 480)
    camera.rotation   = rotationAngle

    print 'camera.resolution: ', camera.resolution
    print 'camera.rotation: ',   camera.rotation
    
    #camera.resolution = (320, 240)
    #camera.framerate = 32
    #camera.framerate = 2
    #rawCapture = PiRGBArray(camera, size=(320, 240))
    
    rawCapture        = PiRGBArray(camera, size=(640, 480))
 
    # allow the camera to warmup
    time.sleep(0.1)

    # moving away from using the frame in the loop:

    while True:
        # grab an image from the camera
        camera.capture(rawCapture, format="bgr")
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


def main():
    # print "Number of arguments", len(sys.argv)
    if len(sys.argv) > 1:
        print 'sys.argv[1]: ', sys.argv[1]
        processAndDisplayImage(rotationAngle=sys.argv[1])
    else:
        processAndDisplayImage(rotationAngle = 0)

if __name__ == '__main__':
    main()

