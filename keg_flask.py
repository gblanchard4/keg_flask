from flask import Flask, render_template, request, jsonify 
import datetime 
import RPi.GPIO as GPIO 
from subprocess import check_output 
import thermometer
import thermostat

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
	thermostat_status =  thermostat.get_state()
	templateData = {
		'title' : 'HELLO!',
		'time' : timeString,
		'temperature' : tempString,
		'thermostat' : thermostat_status
		}
	return render_template('main.html', **templateData)

@app.route("/_temperature")
def _thermostat():
	temp_string = thermometer.read_temp()
	thermostat_status = thermostat.get_state()
	return jsonify(temperature = temp_string, thermostat = thermostat_status)

if __name__ == "__main__":
	try:
		app.run(host='0.0.0.0', port=80, debug=True)
			
	except KeyboardInterrupt:  
		print "Cleaning up"
	
	finally:
		GPIO.cleanup()
