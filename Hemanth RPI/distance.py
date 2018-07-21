import RPi.GPIO as GPIO
import time
import signal
import sys

#When you press Control-C.   Exits the program
def close(signal, frame):
	print("\nTurning off ultrasonic distance detection...\n")
	GPIO.cleanup() 
	sys.exit(0)

signal.signal(signal.SIGINT, close)

def calcDistance():
	# send burst of UV waves
	# set Trigger to HIGH
	GPIO.output(pinTrigger, True)
	time.sleep(0.00001)
	# set Trigger after 0.01ms to LOW
	GPIO.output(pinTrigger, False)

	sendTime = time.time()
	rxTime = time.time()

	# save start time
	while 0 == GPIO.input(pinEcho):
		sendTime = time.time()

	# save time of arrival
	while 1 == GPIO.input(pinEcho):
		rxTime = time.time()

	# time difference between start and arrival
	TimeElapsed = sendTime - rxTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	# Distance = Speed(34300 cm/s) * Time 
	
	distance = round(-1*(TimeElapsed * 34300) / 2, 0)
	
	return distance
	

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# GPIO Pins
pinTrigger = 18
pinEcho = 24
closer = 2
reminder = 3

# set GPIO input and output channels
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(closer, GPIO.OUT)
GPIO.setup(reminder, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

distance = 0
distance2 = 0
x = 0
while True:
	# get distance of object, to check if object coming near or going far
	distance = calcDistance()
	time.sleep(0.05)
	distance2 = calcDistance()
	
	print ("Distance1: "+str(distance)+ " Distance2: "+ str(distance2))
	
	# Usecase1: either of distances < 15 cms.
	if distance < 15 or distance2 < 15:
		print("OBJECT IN CLOSE PROXIMITY")
		# beep, for now turn on the LED <TODO>
	
	# Usecase2: if object is coming very near then start bliking LED plus a sound
	if distance == distance2:
		print("  ")
		GPIO.output(closer, False)
	elif distance - distance2 < 1:
		print ("object is moving further") # stop bliking <TODO>
		GPIO.output(closer, False)
	elif distance - distance2 > -2:
		print("object is moving closer") #start blinking <TODO>
		GPIO.output(closer, True)
	
	# Usecase3: tell user that I am alive, on every 5th min
		# check battery remaining power
	# for now, blink green LED
	if x == 0:
		GPIO.output(reminder, True)
		x = 1
	else:
		GPIO.output(reminder, False)
		x=0
	# Usecase4: get whether updates, on every 10th min, based on the location
	
	# sleep before next iteration
	time.sleep(0.25)
