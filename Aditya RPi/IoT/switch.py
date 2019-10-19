import RPi.GPIO as gp
import time

gp.setwarnings(False)

on = True
off = False
switch = 26
led = 18

gp.setmode(gp.BCM)
gp.setup(led, gp.OUT)
gp.setup(switch, gp.IN)

led_bool = False
last = False

while True:
    if not gp.input(switch) and not last:
        led_bool = False if led_bool else True
        last = True
    elif gp.input(switch):
        last = False

    gp.output(led, led_bool)

    #print(gp.input(switch), led_bool, last)

