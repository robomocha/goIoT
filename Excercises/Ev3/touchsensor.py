#!/usr/bin/env python3
from ev3dev.ev3 import *
import ev3dev.ev3 as ev3

ts = ev3.TouchSensor()
while True:
    ev3.Leds.set_color(ev3.Leds.LEFT, (ev3.Leds.GREEN, ev3.Leds.RED)[ts.value()])