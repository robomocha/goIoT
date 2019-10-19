import picamera
from time import sleep

cam = picamera.PiCamera()

cam.start_preview()

for effect in cam.IMAGE_EFFECTS:
    cam.image_effect = effect
    print(effect)
    cam.annotate_text = "Effect: {}".format(effect)
    sleep(5)

