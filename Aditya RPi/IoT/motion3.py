import RPi.GPIO as gp
import time

pir = 23 # Pin Declarations
led = 24

gp.setmode(gp.BCM)



gp.setup(pir, gp.IN) # Motion sensor - Input
gp.setup(led, gp.OUT) # LED - Output
gp.output(led, False)

while True:
    motion = gp.input(pir) 
    if motion: # If motion has been detected
        print("Motion Detected")
        gp.output(led, True) # Turn on LED for 1 second

    else:
        gp.output(led, False)
        
    time.sleep(0.5)
