import picamera
import time

cam = picamera.PiCamera()
cam.resolution = (640,480)
cam.framerate = 24
cam.start_preview()
cam.annotate_text = str(time.time())
time.sleep(2)

cam.capture('myImage.jpg')
cam.stop_preview()
