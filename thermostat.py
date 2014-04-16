#!/usr/bin/python

'''
Gene Blanchard
'''
import thermometer
import RPi.GPIO as GPIO

def thermostat():

	# Get current temperature
	thermometer.read_temp()
	
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

def main():
	
	try:
		# PowerSwitch Tail II Pin
		power_pin = 23
		# Set the GPIO Mode to BCM
		GPIO.setmode(GPIO.BCM)
		# Setup the power pin, initialize off
		GPIO.setup(power_pin, GPIO.OUT, initial=GPIO.LOW)

	except KeyboardInterrupt:
	# here you put any code you want to run before the program   
	# exits when you press CTRL+C  
	print "\n", counter # print value of counter  
	              except:  
	                  # this catches ALL other exceptions including errors.  
	                      # You won't get any error messages for debugging  
	                          # so only use it once your code is working  
	                              print "Other error or exception occurred!"  
	                                
	                                finally:  
	                                    GPIO.cleanup() # this ensures a clean exit  
	

