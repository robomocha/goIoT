import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)

trig = 18
echo = 24

gp.setup(trig, gp.OUT)
gp.setup(echo, gp.IN)

def distance():
    gp.output(trig, True)

    time.sleep(0.00001)
    gp.output(trig, False)

    start = time.time()
    while gp.input(echo) == 0:
        start = time.time()

    while gp.input(echo) == 1:
        stop = time.time()

    elapsed = stop- start
    return elapsed *34300 / 2

try:
    while True:
        dist = distance()
        print("Distance = %.1f cm"%dist)
except KeyboardInterrupt:
    print('Stopped By User')
    gp.cleanup()

