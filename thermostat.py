#!/usr/bin/python

'''
Gene Blanchard
'''
import thermometer
import RPi.GPIO as GPIO
import time

def thermostat(power_pin):

	# Cast temperature to an int
	temperature = int(float(thermometer.read_temp()))
	
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

def main():

	try:
		# PowerSwitch Tail II Pin
		power_pin = 23
		# Set the GPIO Mode to BCM
		GPIO.setmode(GPIO.BCM)
		# Setup the power pin, initialize off
		GPIO.setup(power_pin, GPIO.OUT, initial=GPIO.LOW)

		# Run the thermostat
		thermostat(power_pin)
		time.sleep(60)		
		
	finally:  
		GPIO.cleanup() # this ensures a clean exit  

if __name__ == "__main__":
	main()
