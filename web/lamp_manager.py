#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def lamp_control(pin):
    state = lamp_status(pin)
    if state == 1:
        GPIO.setup(pin, GPIO.LOW)
    else:
        GPIO.setup(pin, GPIO.HIGH)


def lamp_status(pin):
    status = GPIO.input(pin)
    return status