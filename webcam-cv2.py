# Copied this from the web site:
#
# https://gist.github.com/tedmiston/6060034
#
# I was looking for examples of grabbing images from a web camera
# connected to the USB port of my Raspberry Pi Zero.
# In it's present form the program started grabbing images from my
# USB camera connected to the Raspberry Pi Zero. I suspect this same
# code would work equally well on a Raspberry Pi 2/3/or 4.

# This was only grabbing images from the USB camera when I specified
# VideoCapture(1). When I specified VideoCapture(0) it grabbed from the
# RaspberryPi Camera.

"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

import cv2

def show_webcam(mirror=False):
    cam0 = cv2.VideoCapture(0)
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
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()

