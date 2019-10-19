import picamera
from time import sleep

camera = picamera.PiCamera()

camera.led = True
sleep(5)
camera.led = False

camera.capture('camera8.jpg')



