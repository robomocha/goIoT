import RPi.GPIO as gp
import time

on = True
off = False

gp.setmode(gp.BCM)
gp.setup(18, gp.OUT)

gp.output(18, on)

time.sleep(5)
print("Off")
gp.output(18, off)



