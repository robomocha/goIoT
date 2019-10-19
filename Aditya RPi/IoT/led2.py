import RPi.GPIO as gp
import time

on = True
off = False

gp.setmode(gp.BCM)
led = 18
gp.setup(led, gp.OUT)
while True:

    gp.output(led, on)

    time.sleep(0.5)

    gp.output(led, off)
    
    time.sleep(0.5)



