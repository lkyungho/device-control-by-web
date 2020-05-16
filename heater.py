#!/usr/bin/python3

import RPi.GPIO as GPIO
import cgi, cgitb

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

form = cgi.FieldStorage()
heatstat = form.getvalue("led1")

print ("Content-type: text/html\n\n")
if(heatstat != None):
	if(heatstat == "power_on"):
		heater_power = 1
		print ("Heater is ON")
	else:
		heater_power = 0
		print ("Heater is OFF")
	GPIO.output(18, heater_power)
else:
	if(GPIO.input(18) == 1):
		print ("Heater is ON")
	else:
		print ("Heater is OFF")
