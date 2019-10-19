from time import sleep
from picamera import PiCamera
from fractions import Fraction

camera = PiCamera()

camera.resolution = (1280, 720)
camera.framerate = 1/6
camera.sensor_mode = 3

camera.shutter_speed = 60000000
camera.iso = 100

camera.start_preview()
sleep(5)

camera.exposure_mode = 'off'
camera.capture('dark.jpg')

camera.stop_preview()

