import RPi.GPIO as GPIO
import time
import signal
import sys

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
pinTrigger = 18
pinEcho = 24
closer = 2
def close(signal, frame):
	print("\nTurning off ultrasonic distance detection...\n")
	GPIO.cleanup() 
	sys.exit(0)

signal.signal(signal.SIGINT, close)

# set GPIO input and output channels
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(closer, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)
distance = 0
distance2 = 0
while True:
	for x in range (2):
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
		if x == 1:
			distance = round((TimeElapsed * 34300) / 2, 0)
		else:
			distance2 = round((TimeElapsed *34300)/2,0)
			print ("Distance1: "+str(distance)+ "Distance2: "+ str(distance2))
		time.sleep(0.25)

	if distance - distance2 > 5:
		print ("object is moving further")
		GPIO.output(closer, False)
	elif distance - distance2 < -5:
		print("object is moving closer")
		GPIO.output(closer, True)

