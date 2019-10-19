from time import sleep
from picamera import PiCamera

camera  = PiCamera()

camera.resolution = (1024, 768)
camera.start_preview()

sleep(2)
camera.capture('im1.jpg', resize=(320, 240))
camera.capture('im2.jpg')

camera.stop_preview()
