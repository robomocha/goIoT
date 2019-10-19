# RPi motion sensor with the buzzer

import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(23, gp.IN) # Motion sensor
gp.setup(24, gp.OUT) # Buzzer

try:
    time.sleep(2)
    while True:
        if gp.input(23): # If motion, play buzzer
            gp.output(24, True)
            time.sleep(0.5) # buzzer on for 0.5 sec
            gp.output(24, False)
            print("Motion")
            time.sleep(1) # Sleep for a second to prevent double readings
        time.sleep(0.1) # Loop delay

except: # Program is stopped: 
    gp.cleanup() # Finish up
