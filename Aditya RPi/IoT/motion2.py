# RPi motion sensor with the buzzer

import RPi.GPIO as gp
import time

gp.setwarnings(False)

gp.setmode(gp.BCM)
gp.setup(23, gp.IN) # Motion sensor
gp.setup(24, gp.OUT) # LED


try:
    time.sleep(2)
    while True:
        if gp.input(23): # If motion,
            gp.output(24, True)
            print("Motion")
            time.sleep(1) # Sleep for a second to prevent double readings
        else:
            gp.output(24, False)
            print("No Motion")
        time.sleep(0.1) # Loop delay

except: # Program is stopped: 
    gp.cleanup() # Finish up

