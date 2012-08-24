#! /usr/bin/python

import os
from serial import Serial
import requests
import xml.etree.cElementTree as xml
from PyDateTime import DateTime

def getDateTime(root, namespace):
	dateTime = DateTime()
	date = root.find('./%sob/%sob-date' % (namespace, namespace))
	dateTime.month = date.find('./%smonth' % namespace).get('number')
	dateTime.day = date.find('./%sday' % namespace).get('number')
	dateTime.year = date.find('./%syear' % namespace).get('number')
	dateTime.hour = date.find('./%shour' % namespace).get('number')
	dateTime.minute = date.find('./%sminute' % namespace).get('number')
	dateTime.second = date.find('./%ssecond' % namespace).get('number')
	
	return dateTime
	
def getSunrise(root, namespace):
	dateTime = DateTime()
	sunrise = root.find('./%sob/%ssunrise' % (namespace, namespace))
	dateTime.month = sunrise.find('./%smonth' % namespace).get('number')
	dateTime.day = sunrise.find('./%sday' % namespace).get('number')
	dateTime.year = sunrise.find('./%syear' % namespace).get('number')
	dateTime.hour = sunrise.find('./%shour' %  namespace).get('number')
	dateTime.minute = sunrise.find('./%sminute' %  namespace).get('number')
	dateTime.second = sunrise.find('./%ssecond' %  namespace).get('number')
	
	return dateTime

def getSunset(root, namespace):
	dateTime = DateTime()
	sunset = root.find('./%sob/%ssunset' % (namespace, namespace))
	dateTime.month = sunset.find('./%smonth' % namespace).get('number')
	dateTime.day = sunset.find('./%sday' % namespace).get('number')
	dateTime.year = sunset.find('./%syear' % namespace).get('number')
	dateTime.hour = sunset.find('./%shour' %  namespace).get('number')
	dateTime.minute = sunset.find('./%sminute' %  namespace).get('number')
	dateTime.second = sunset.find('./%ssecond' %  namespace).get('number')

	return dateTime

def doWeatherBug(url, namespace):
	response = requests.get(url)

	root = xml.fromstring(response.text)

	dateTime = getDateTime(root, namespace)
	print dateTime.toString()

	sunrise = getSunrise(root, namespace)
	sunset = getSunset(root, namespace)
	print sunrise.toString()
	print sunset.toString()

	return "%s,%s,%s" % (dateTime.toCsv(), sunrise.toCsv(), sunset.toCsv())


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
