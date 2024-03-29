# This example was grabbed from:
# https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
# it worked to grab a video stream and display it
# When reduced to a 320x240 image at 16 frames per second I was seeing
# about a 1 second delay and about 80% of the CPU.
# As I'm running on a remote desktop some of the delay may in fact
# be due to trying to move the images from the Pi to my desktop computer


# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# original code was using a 640 x 480 image and had
# about 1-2 seconds of delay.

def display_images():
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(640, 480))
        
        cam0 = cv2.VideoCapture(0)

        # allow the camera to warmup
        time.sleep(0.1)

        # In the webcam-cv2 the loop is a forever loop where cam0,
        # an instantiation of cv2.VideoCapture(x) is used to read an
        # image from a usb camera.
        
        # capture frames from the camera
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	        # grab the raw NumPy array representing the image, then initialize the timestamp
	        # and occupied/unoccupied text
	        image = frame.array

                ret_val0, img0 = cam0.read();
        
	        # show the frame

                # This is the same function as used in the webcam-cv2.py
                # example code for displaying the image in a frame.
                
#	        cv2.imshow("Frame    ", image)
                cv2.imshow("Web Cam 0", img0)
        
	        key = cv2.waitKey(1) & 0xFF
 
	        # clear the stream in preparation for the next frame
	        rawCapture.truncate(0)
 
	        # if the `q` key was pressed, break from the loop
	        if key == ord("q"):
		        break
        cv2.destroyAllWindows()

def main():
    display_images()


if __name__ == '__main__':
    main()

