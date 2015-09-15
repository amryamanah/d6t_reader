# ! /usr/bin/env python

import RPi.GPIO as GPIO
import time

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

# Turn GPIO 11 to high
GPIO.output(11, GPIO.HIGH)

# Sleep for 5 second
time.sleep(5)

# Turn GPIO 11 off
GPIO.output(11, GPIO.LOW)

GPIO.cleanup()