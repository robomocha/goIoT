from time import sleep
from picamera import PiCamera

cam = PiCamera()
cam.start_preview()

sleep(2)

for c, filename in enumerate(cam.capture_continuous('img{counter:03d}.jpg')):
    print(c)
    print('Captured {}'.format(filename))
    sleep(1)

    if c >= 9:
        cam.stop_preview()
        print('done')
        break


