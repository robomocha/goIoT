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
	# set Trigger to HIGH
	GPIO.output(pinTrigger, True)
	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(pinTrigger, False)

	startTime = time.time()
	stopTime = time.time()

	# save start time
	while 0 == GPIO.input(pinEcho):
		startTime = time.time()

	# save time of arrival
	while 1 == GPIO.input(pinEcho):
		stopTime = time.time()

	# time difference between start and arrival
	TimeElapsed = stopTime - startTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	# Distance = Speed(34300 cm/s) * Time 
	
	distance = round((TimeElapsed * 34300) / 2, 0)
	
	return distance
	

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
pinTrigger = 18
pinEcho = 24
closer = 2

# set GPIO input and output channels
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(closer, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)
distance = 0
distance2 = 0

while True:	
	distance = calcDistance()
	time.sleep(0.05)
	distance2 = calcDistance()
	print ("Distance1: "+str(distance)+ "Distance2: "+ str(distance2))
	time.sleep(0.25)
	
	if distance < 15 or distance2 < 15:
		print("OBJECT IN CLOSE PROXIMITY")
	if distance - distance2 > 1:
		print ("object is moving further")
		GPIO.output(closer, False)
	elif distance - distance2 < -2:
		print("object is moving closer")
		GPIO.output(closer, True)

