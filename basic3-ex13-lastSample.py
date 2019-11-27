import socket
import time
import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('wb')
try:
    camera.start_recording(connection, format='h264')
    camera.wait_recording(60)
    camera.stop_recording()
finally:
    connection.close()
    server_socket.close()
    
# To use this first run this program, I have used it with python 3
# and then issue the command:
# vlc tcp/h264://raspberrypi-zero-3.local:8000/
# This complains a lot - but does at least display the image from
# the camera on my remote display.
#
# The local IP address used above 'raspberrypi-zero-3.local' will need
# be changed for the IP address of the machine this is run on.
#
# Doesn't work very good, crashed after a few seconds.
