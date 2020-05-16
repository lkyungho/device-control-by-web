# Web Based Temperature Control System

This project is a remote temperature control system. Users can control temperature from anywhere without being present at an actual place. A temperature sensor can detect the current temperature and send data to the Raspberry Pi to notify the temperature information. Then, the Raspberry Pi transfers data via the Internet so that users can figure out temperature of their desired places and determine which devices they will use.

```
* Hardware: Raspberry Pi, DHT22(temperature and humidity sensor), LCD, Circuit design
* Software: Linux OS, Python, HTML, CSS, AJAX, CGI, AWS
```

## _1. System Diagram_
The base information of the system is temperature data from a DHT22 sensor. **`Acquisition.py`** acquires temperature data, which uses Adafruit DHT Humidity & Temperature Sensor Library. **`Acquisition.py`** distributes temperature data all over the system. **`dht22_project.htm`** is executed on a web browser. This module receives current temperature data from **`currentTemp.py`** and controls devices through network. **`DHT22AWS.py`** publishes current temperature information to AWS(Cloud service). Finally, **`tempInfoLCD.py`** operates a LCD device to show temperature to users.
![alt text](https://github.com/lkyungho/Images/blob/master/temperature-control-diagram.JPG "System Diagram")
