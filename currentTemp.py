#!/usr/bin/python3

import sys
sys.path.insert(0,"/home/pi/PROJECT")
from Acquisition import read_data
temp, humid = read_data()

print ("Content-type: text/html\r\n\r\n")
print ("%.1f" % temp)
