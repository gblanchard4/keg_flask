#!/usr/bin/python

'''
Gene Blanchard
'''
import sys
import thermometer
import RPi.GPIO as GPIO
import time
import os
import numpy as np
import datetime
import ConfigParser
from daemon import Daemon

# Set the woking directory where the daemon is
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Get the values from the config file
config = ConfigParser.ConfigParser()
config.read("config.txt")
DEBUG = int(config.get('main','DEBUG'))
target_high = float(config.get('main','target_high'))
target_low = float(config.get('main','target_low'))
target_range = np.arange(target_low,target_high+1) 
POWER_PIN = int(config.get('main','POWER_PIN'))
errorThreshold = float(config.get('main','errorThreshold'))


class thermostatDaemon(Daemon):

	def configureGPIO(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(POWER_PIN, GPIO.OUT, initial=GPIO.LOW)
		subprocess.Popen("echo " + str(POWER_PIN) + " > /sys/class/gpio/export", shell=True)

	def getPowerswitchStatus(self):
		powerswitchStatus = GPIO.input(POWER_PIN)
		return powerswitchStatus

	def turn_on(self):
		GPIO.output(POWER_PIN, True)
		return 1
		
	def turn_off(self):
		GPIO.output(POWER_PIN, False)
		return -1
		
	def run(self):
		lastLog	= datetime.datetime.now()
		
		# Configure GPIO
		self.configureGPIO()
		
		while True:
		
			# Change cwd to thermostat daemon
			abspath = os.path.abspath(__file__)
			dname = os.path.dirname(abspath)
			os.chdir(dname)
			
			# Get the current temperature 
			current_temp =  float(temperature.read_temp())
						
			# Get the powerswitch state
			powerswitchState = int(getPowerswitchStatus())
		
			now = datetime.datetime.now()
			
			if current_temp > target_range[-1]:
				self.turn_on()

			if current_temp < target_range[0]:
				self.turn_off()
				
			time.sleep(60)
	

if __name__ == "__main__":
	daemon = thermostatDaemon('thermostatDaemon.pid')
	
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(POWER_PIN, GPIO.OUT)
			GPIO.output(POWER_PIN, False)
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
		
