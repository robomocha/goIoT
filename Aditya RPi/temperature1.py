from time import sleep
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

while True:
    temp  = sensor.get_temperature()
    print("The temperature is {}".format(temp))
    sleep(1)
