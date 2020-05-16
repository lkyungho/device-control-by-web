#!/usr/bin/python3

import RPi.GPIO as GPIO
import cgi, cgitb

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

form = cgi.FieldStorage()
coolstat = form.getvalue("led2")

print ("Content-type: text/html\n\n")
if(coolstat != None):
	if(coolstat == "power_on"):
		cooler_power = 1
		print ("Cooler is ON")
	else:
		cooler_power = 0
		print ("Cooler is OFF")
	GPIO.output(23, cooler_power)
else:
	if(GPIO.input(23) == 1):
		print ("Cooler is ON")
	else:
		print ("Cooler is OFF")
