import picamera
import datetime as dt
import time

with picamera.PiCamera() as cam:
    cam.resolution = (1280,720)
    cam.framerate = 24
    cam.start_preview()
    cam.annotate_background = picamera.Color('black')
    cam.annotate_text = dt.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    cam.start_recording('timestamped.h264')
    start = dt.datetime.now()
    c = 0
    while (dt.datetime.now() - start).seconds < 30:
        c += 1
        cam.annotate_text = dt.datetime.now().strftime('%Y-%m-%d%H:%M:%S')    
        #cam.stop_preview()
    cam.stop_recording()
