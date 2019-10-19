from time import sleep
import RPi.GPIO as gp

red = 21
green = 20
blue = 16

gp.setmode(gp.BCM)

running = True

gp.setup(red, gp.OUT)
gp.setup(green, gp.OUT)
gp.setup(blue, gp.OUT)

freq = 100

RED = gp.PWM(red, freq)
GREEN = gp.PWM(green, freq)
BLUE = gp.PWM(blue, freq)

try:
    while running:
        RED.start(100)
        GREEN.start(1)
        BLUE.start(1)

        for i in range(1, 101):
            GREEN.ChangeDutyCycle(101-i)
            sleep(0.025)

        for i in range(1, 101):
            RED.ChangeDutyCycle(i)
            sleep(0.025)

        for i in range(1, 101):
            BLUE.ChangeDutyCycle(101-i)
            sleep(0.025)
            
except KeyboardInterrupt:
    running = False
    gp.cleanup()
    
