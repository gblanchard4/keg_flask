from flask import Flask, render_template, request, jsonify 
import datetime 
import RPi.GPIO as GPIO 
from subprocess import check_output 
import thermometer

app = Flask(__name__)

@app.route("/")

def Index():
	return render_template("index.html", uptime=GetUptime())

def GetUptime():
	output =  check_output(["uptime"])
	uptime =  output[output.find("up"):output.find("user")-5]
	return uptime
	
@app.route("/hello")
def hello():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")
	tempString = thermometer.read_temp()
	thermostat_status = open('/sys/class/gpio/gpio23/value', 'r').readline()
	if thermostat_status.rstrip() == '1':
		thermostat_string = "ON"
	if thermostat_status.rstrip() == '0':
		thermostat_string == "OFF"
	print thermostat_string
	templateData = {'title' : 'HELLO!',	'time' : timeString,'temperature' : tempString, 'thermostat' : thermostat_string}
	return render_template('main.html', **templateData)

@app.route("/_temperature")
def thermostat():
	temp_string = thermometer.read_temp()
	thermostat_status = open('/sys/class/gpio/gpio23/value', 'r').readline()
	if thermostat_status.rstrip() == '1':
		thermostat_string = "ON"
	if thermostat_status.rstrip() == '0':
		thermostat_string == "OFF"
	return jsonify(temperature = temp_string, thermostat = thermostat_string)


if __name__ == "__main__":
	try:
		app.run(host='0.0.0.0', port=80, debug=True)
			
	except KeyboardInterrupt:  
		print "Cleaning up"
	
	finally:
		GPIO.cleanup()
