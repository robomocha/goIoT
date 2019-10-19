import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)

gp.setup(18, gp.OUT)
pwm = gp.PWM(18, 100)

dc = 0
pwm.start(dc)

while True:
    for dc in range(0, 101, 5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.05)
        print(dc)
    for dc in range(95, 0, -5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.05)
        print(dc)

pwm.stop()
gp.cleanup()

