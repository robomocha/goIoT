from time import sleep
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.raw_format = 'rgb'
    camera.start_preview()
    sleep(2)
    camera.capture('image.data', 'raw')
    
camera.stop_preview()
