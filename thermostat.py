#!/usr/bin/python

'''
Gene Blanchard
'''

import RPi.GPIO as GPIO
import math

def setup():
	# PowerSwitch Tail II Pin
	power_pin = 23
	# Set the GPIO Mode to BCM
	GPIO.setmode(GPIO.BCM)
	# Setup the power pin
	GPIO.setup(power_pin, GPIO.OUT)

def getState():
	return str(GPIO.input(power_pin))

if __name__ == '__main__':
	setup()
