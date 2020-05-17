# Web Based Temperature Control System

This project is a remote temperature control system, which is an integrated system. Users can control temperature from anywhere without being present at an actual place. A temperature sensor can detect the current temperature and send data to the Raspberry Pi to notify the temperature information. Then, the Raspberry Pi transfers data via the Internet so that users can figure out temperature of their desired places and determine which devices they will use.

```
* Hardware: Raspberry Pi, DHT22(temperature and humidity sensor), LCD, Circuit design
* Software: Linux OS, Python, HTML, CSS, AJAX, CGI, AWS
```

## _1. System Diagram_
The base information of the system is temperature data from a DHT22 sensor. **`Acquisition.py`** acquires temperature data, which uses Adafruit DHT Humidity & Temperature Sensor Library. **`Acquisition.py`** distributes temperature data all over the system. **`dht22_project.htm`** is executed on a web browser. This module receives current temperature data from **`currentTemp.py`** and controls devices through network. **`DHT22AWS.py`** publishes current temperature information to AWS(Cloud service). Finally, **`tempInfoLCD.py`** operates a LCD device to show temperature to users.
![alt text](https://github.com/lkyungho/Images/blob/master/temperature-control-diagram.JPG "System Diagram")
## _2. Descriptions of the System_
### (1) Temperature data acquisition
#### - DHT22 Temperature and Humidity Sensor
DHT22 sensor is a versatile temperature and humidity sensor, which has built-in analog to digital converter (ADC).
#### - Acquision.py
Adafruit DHT Python library is used to interact with the DHT22 temperature and humidity sensor.
(Link: [Adafruit_Python_DHT](https://github.com/adafruit/Adafruit_Python_DHT))
**`read_retry`** method from **`Adafruit_Python_DHT/Adafruit_DHT/common.py`** is used for data acquisition.
```python
def read_data():
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	return temperature, humidity
```
### (2) Temperature Control Through a Web Browser
Users can access the system through a web browser to control temperature. AJAX (Asynchronous JavaScript and XML), HTML (HyperText Markup Language) and CSS (Cascading Style Sheets) are used for user interaction.
#### - dht22_project.htm
There are three parts that show up on the web page; **`Current temperature`**, **`Automatic temperature control`**, and **`Manual device control`**. 
> [Current temperature]
>
>the current temperature data is acquired from **`Acquisition.py`** and temperature information is displayed.

> [Automatic temperature control]
>
> The heating device or the cooling device is turned on to maintain the target temperature when a target temperature is set. The manual operation is disabled while this part is activated.

> [Manual device control]
>
> User can turn on and off for all the device. One of the heating device and the cooling device is off when the other is on. Automatic temperature control part is disabled while Manual device control part is activated.
