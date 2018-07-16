import numpy as np
import picamera as pic
import picamera.array as pia
from time import sleep 

#the motion dectection helping class 
class DetectMotion(pia.PiMotionAnalysis):
    def analyse(self,a):
        a = np.sqrt(
            np.square(a['x'].astype(np.float)) +
            np.square(a['y'].astype(np.float))
            ).clip(0,255).astype(np.uint8)

        if(a>60).sum() >10:
            print("there is a moving object near your house")
            
choice = input("Motion dectector[1] or Patio Watcher[2]")

if(choice == "1"):
    with pic.PiCamera() as camera:
        with DetectMotion(camera) as output:
            camera.resolution =(640,480)
            camera.start_recording(
                '/dev/null',format='h264', motion_output = output)
            camera.wait_recording(10)
            camera.stop_recording()
elif(choice == "2"):
    with pic.PiCamera() as camera:
        camera.resolution =(640,480)
        for x in range(1,50):
            camera.capture("%s.jpg")
            sleep(5)

