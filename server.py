# -- coding: utf-8 --

__author__ = 'amryfitra'

import RPi.GPIO as GPIO
import time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/measure_temp")
def measure_temp():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    
    # Turn GPIO 11 to high
    GPIO.output(11, GPIO.HIGH)

    # Sleep for 5 second
    time.sleep(5)

    # Turn GPIO 11 off
    GPIO.output(11, GPIO.LOW)

    GPIO.cleanup()

    # Put function to measured data
    return "finish"

@app.route("/get_temp_data")
def get_temp_data():
    # put function to download data
    return "Function holder to download data"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
