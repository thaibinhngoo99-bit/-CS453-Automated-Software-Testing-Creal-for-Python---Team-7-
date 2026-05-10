#!/usr/bin/env python

import time

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.LOW)

time.sleep(3.00)

GPIO.output(21, GPIO.HIGH)
GPIO.cleanup()

