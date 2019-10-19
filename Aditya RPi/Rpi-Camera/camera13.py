import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.framerate = 30

    camera.start_preview()
    time.sleep(2)
    camera.capture_sequence(['image{}'.format(i) for i in range(1, 6)])
