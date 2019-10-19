import numpy as np
import picamera
import picamera.array
import time

motion = False

class DetectMotion(picamera.array.PiMotionAnalysis):
    def analyse(self, a):
        global motion
        a = np.sqrt(
                np.square(a['x'].astype(np.float))+
                np.square(a['y'].astype(np.float))
                ).clip(0,255).astype(np.uint8)

        if (a>60).sum() > 10:
            print('motion')
            motion = True

        else:
            motion = False

with picamera.PiCamera() as camera:
    with DetectMotion(camera) as output:
        camera.resolution = (640, 480)
        print('before recording')
        camera.start_recording(
                    '/dev/null',format='h264',motion_output=output)
        print('after')
        camera.start_preview()
        start = time.time()
        while time.time() - start < 10:
            camera.annotate_text = "Motion: {}".format(motion)
            camera.wait_recording(0.2)
        camera.stop_recording()
        camera.stop_preview()
