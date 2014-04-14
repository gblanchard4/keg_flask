from flask import Flask, render_template, request, jsonify
import datetime
import RPi.GPIO as GPIO
from subprocess import check_output
import thermometer

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

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
	templateData = {
		'title' : 'HELLO!',
		'time' : timeString,
		'temperature' : tempString
		}
	return render_template('main.html', **templateData)

@app.route("/_temperature")
def _temperature():
	temp_string = thermometer.read_temp()
	return jsonify(temperature = temp_string)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
