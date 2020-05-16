#!/usr/bin/python3

import time
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def read_data():
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	return temperature, humidity

if __name__ == '__main__':
	while(True):
		temp, humid = read_data()
		if (humid != None and temp != None):
			print ("Temp = {1:0.1f}degC  Humidity = {1:0.1f}%".format(temp,humid))
			time.sleep(1)
		else:
			print ("Failed to retrieve data from the sensor")
