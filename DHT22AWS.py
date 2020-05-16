#!/usr/bin/python3

# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
# Import time to generate time delay between messages
import time
# Import temerature measurement data
from Acquisition import read_data

# this function is called when a message is posted to the Raspberry Pi
messageIn = "empty"
def customCallback( client, userdata, message ):
	print( "From Topic: " )
	print( message.topic )
	print( "Message: " )
	print( message.payload )
	global messageIn
	messageIn = message.payload

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("DeviceName")

# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("RestAPIEnpoint", 8883)
myMQTTClient.configureCredentials("RootCaFileName", "PrivateKeyFileName", "CertFileName")
myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
# Connect to AWS IoT
myMQTTClient.connect()

# Subscribe to AWS IoT Topic to receive message posted sdkTest/sub
myMQTTClient.subscribe("DHT22_project/sub", 1, customCallback)

# Loop post message to sdkTest/pub topic every 30 seconds
while messageIn !="quit":
	Temp, Humid = read_data()
	if (Temp != None and Humid != None):
		myMQTTClient.publish("DHT22_project/pub", "Temperature: %.1f (degC)"%Temp, 0)
		time.sleep(30)
	else:
		myMQTTClient.publish("DHT22_project/pub", "Fail to retrieve data", 0)
