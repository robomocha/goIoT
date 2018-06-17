#!/usr/bin/env python3
# created by goviraja on 01/12/2018 


from ev3dev.ev3 import *
import ev3dev.ev3 as ev3

#ev3.Sound.speak('Hi welcome to RoboMocha').wait()

mm = ev3.MediumMotor()
mm.run_to_rel_pos(speed_sp=700, position_sp=-1000)

while 'running' in mm.state:
	time.sleep(0.1)
