#! /usr/bin/python

import os
from serial import Serial
import requests
import xml.etree.cElementTree as xml
import time
from PyDateTime import DateTime

def getDateTime(whichDate, root, namespace):
	dateTime = DateTime()
	date = root.find('./%sob/%s%s' % (namespace, namespace, whichDate))
	dateTime.month = date.find('./%smonth' % namespace).get('number')
	dateTime.day = date.find('./%sday' % namespace).get('number')
	dateTime.year = date.find('./%syear' % namespace).get('number')
	dateTime.hour = date.find('./%shour' % namespace).get('number')
	dateTime.minute = date.find('./%sminute' % namespace).get('number')
	dateTime.second = date.find('./%ssecond' % namespace).get('number')
	dateTime.dayOfWeek = (time.localtime()).tm_wday
	dateTime.dayOfYear = (time.localtime()).tm_yday
	dateTime.daylightSavings = (time.localtime()).tm_isdst

	return dateTime
	
def doWeatherBug(url, namespace):
	response = requests.get(url)

	root = xml.fromstring(response.text)

	dateTime = getDateTime('ob-date', root, namespace)
	print dateTime.toString()

	sunrise = getDateTime('sunrise', root, namespace)
	sunset = getDateTime('sunset', root, namespace)
	print sunrise.toString()
	print sunset.toString()

	return "%d,%d,%d" % (int(dateTime.inSeconds()), int(sunrise.inSeconds()), int(sunset.inSeconds()))


os.seteuid(0)

serial = Serial(0, 9600)

namespace = "{http://www.aws.com/aws}"
apicode = "A4537183367"
zipcode = "24060"
unitType = "0"
outputType = "1"
url = "http://api.wxbug.net/getLiveWeatherRSS.aspx?ACode=" + apicode + "&zipCode=" \
 + zipcode + "&UnitType=" + unitType +  "&OutputType=" + outputType

if(__name__ == '__main__'):
	while(True):
		if(int(serial.readline()) == 1):
			serialString = doWeatherBug(url, namespace)
			serial.write(serialString)
