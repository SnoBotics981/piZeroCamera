# Copied this from the web site:
#
# https://gist.github.com/tedmiston/6060034
#
# This example, as modified by Rob Steele is working to grab a video
# stream from my Orion Telescope camera.
#
# At the default values it was using 100% of the CPU.
"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

import cv2

def show_webcam(mirror=False):
    cam1 = cv2.VideoCapture(1)
    while True:
        ret_val1, img1 = cam1.read()
        if mirror: 
            img1 = cv2.flip(img1, 1)
        cv2.imshow('my webcam 1', img1)
       	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop

	if key == ord("q"):
		break
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()

