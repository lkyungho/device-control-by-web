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
### (1) Temperature Data Acquisition
#### - DHT22 temperature and humidity sensor
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
### (2) Temperature Monitoring
Temperature is displayed through a LCD device and AWS (Cloud service).
#### - LCD device
A 16 x 2 LCD (NHD‐0216BZ‐FL‐YBW) device is used to display current temperature data.

**`tempInfoLCD.py`** uses methods from **`lcd.py`** _(For more information about_ **`lcd.py`**_: [16×2 LCD Module Control Using Python](https://www.raspberrypi-spy.co.uk/2012/07/16x2-lcd-module-control-using-python))_
#### - Publishing temperature data to AWS
To publish or subscribe topic and payload to AWS, MQTT (Message Queuing Telemetry Transport) protocol is used and a Raspberry Pi works as a broker.

**`DHT22AWS.py`** obtains temperature data from **`Acquisition.py`**. Topic name is `DHT_project/pub` and message is current temperature information.

### (3) Temperature Control Through a Web Browser
Users can access the system through a web browser to control temperature. AJAX, HTML and CSS are used for user interaction.
#### - dht22_project.htm
There are three parts that show up on the web page; **`Current temperature`**, **`Automatic temperature control`**, and **`Manual device control`**. 
> **[Current temperature]**
>
>the current temperature data is acquired from **`Acquisition.py`** and temperature information is displayed.

> **[Automatic temperature control]**
>
> A heating device or a cooling device is turned on to maintain a target temperature when the target temperature is set. The manual operation is disabled while this part is activated.

> **[Manual device control]**
>
> User can turn on and off for the devices manually. When one of the heating device and the cooling device is on, the other is off. Automatic temperature control part is disabled while Manual device control part is activated.

![alt text](https://github.com/lkyungho/Images/blob/master/temperature-control-web.JPG "Web control")

## _3. Result_
### (1) Wiring of the Devices
For demonstration purpose, the wiring for the heating device and the cooling device is connected to LEDs.

![alt text](https://github.com/lkyungho/Images/blob/master/temperature-control-wiring.JPG "Wiring")

### (2) Web Page
#### - Target temperature setting and device control
When the current temperature is lower than the set temperature, the heating device is ON and the cooling device is OFF. When the current temperature is higher than the set temperature, the cooling device is ON and the heating device is OFF.
#### - Manual Device Control
If manual device control is activated, automatic temperature control is disabled. Also, when one of the heating device and the cooling device is ON, the other is OFF.

![alt text](https://github.com/lkyungho/Images/blob/master/temperature-control-webpage.JPG "Web page")
