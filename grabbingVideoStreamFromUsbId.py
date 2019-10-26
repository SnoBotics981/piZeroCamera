
"""
Copied this from the web site:

https://gist.github.com/tedmiston/6060034

This example, as modified by Rob Steele is working to grab a video
stream a single specified USB port. For the Raspberry Pi Zero the
Raspberry Pi camera is located as Port number 0.

10/25/19: Working to grab the Raspberry Pi camera on usb 0. In my experiments
with the cameras the raspberry pi camera is always on id 0.

At the default values it was using 100% of the CPU on the Pi Zero.

10/25/19: When run on the Pi 4 the high resolution camera, the program
crashed. The dump looked like:

python grabbingVideoStreamFromUsbId.py 1&
[3] 2541
pi@raspberrypi4-1:~/git/piZeroCamera $ Unable to stop the stream: Invalid argument
OpenCV Error: Assertion failed (size.width>0 && size.height>0) in imshow, file /build/opencv-L65chJ/opencv-3.2.0+dfsg/modules/highgui/src/window.cpp, line 304
Traceback (most recent call last):
  File "grabbingVideoStreamFromUsbId.py", line 44, in <module>
    main()
  File "grabbingVideoStreamFromUsbId.py", line 39, in main
    show_webcam(mirror=True,usbId=sys.argv[1])
  File "grabbingVideoStreamFromUsbId.py", line 25, in show_webcam
    cv2.imshow('my webcam 0', img0)
cv2.error: /build/opencv-L65chJ/opencv-3.2.0+dfsg/modules/highgui/src/window.cpp:304: error: (-215) size.width>0 && size.height>0 in function imshow
"""


"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

import sys
import cv2

def show_webcam(mirror=False,usbId=1):
    # print 'usbId: ', usbId
    cam0 = cv2.VideoCapture(int(usbId))
    while True:
        ret_val0, img0 = cam0.read()
        if mirror: 
            img0 = cv2.flip(img0, 1)
        cv2.imshow('my webcam 0', img0)
       	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop

	if key == ord("q"):
		break
    cv2.destroyAllWindows()


def main():
    # print "Number of arguments", len(sys.argv)
    if len(sys.argv) > 1:
        # print 'sys.argv[1]: ', sys.argv[1]
        show_webcam(mirror=True,usbId=sys.argv[1])
    else:
        show_webcam(mirror=True)

if __name__ == '__main__':
    main()

