#!/usr/bin/python3

import time
#import RPi.GPIO as GPIO
import lcd
from Acquisition import read_data 

lcd.lcd_init()
LINE1 = lcd.LCD_LINE_1
LINE2 = lcd.LCD_LINE_2
CMD = lcd.LCD_CMD
CHR = lcd.LCD_CHR

try:
	while True:
		temp, humid = read_data()
		if(temp == None or humid == None):
			lcd.lcd_byte(0x01, CMD)
			lcd.lcd_string("Retrieving data..", LINE1)
			time.sleep(1)
		else:
			lcd.lcd_byte(0x01, CMD)
			lcd.lcd_string("Temperature", LINE1)
			lcd.lcd_string("%.1f degC" % temp, LINE2+1)
			time.sleep(3)

			lcd.lcd_byte(0x01, CMD)
			lcd.lcd_string("Humidity", LINE1)
			lcd.lcd_string("%.1f" % humid, LINE2+1)
			lcd.lcd_string("%", LINE2+6)
			time.sleep(1)

except KeyboardInterrupt:
	print("\nKeyboard Interrupt")
finally:
	lcd.lcd_byte(0x01, CMD)
	lcd.lcd_string("Good-bye", LINE1)
	time.sleep(3)
	lcd.lcd_byte(0x01, CMD)
