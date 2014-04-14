#!/usr/bin/python

'''
Gene Blanchard
'''
import thermometer
import RPi.GPIO as GPIO

# PowerSwitch Tail II Pin
power_pin = 23
# Set the GPIO Mode to BCM
GPIO.setmode(GPIO.BCM)
# Setup the power pin, initialize off
GPIO.setup(power_pin, GPIO.OUT, initial=GPIO.LOW)

def thermostat(temperature):

	# Cast temperature to an int
	temperature = int(float(temperature))
	
	# Optimal beer temperature is 50-55
	beer_range = range(50,56) # 50-55F
	
	# If the temperature is too high
	if temperature > beer_range[-1]:
		# Turn the fridge on
		GPIO.output(power_pin, True)
	
	# If the temperature is too low
	if temperature < beer_range[0]:
		# Turn the fidge off
		GPIO.output(power_pin, False)
	
def get_state():
	return str(GPIO.input(power_pin))	

