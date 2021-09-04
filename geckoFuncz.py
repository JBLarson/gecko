#!/usr/bin/python3

import time
import datetime
import requests
import json



def unixToDatetime(epochTime):
	localTime = time.strftime('%Y-%m-%d', time.localtime(epochTime))

	return localTime



def datetimeToUnix(ogDatetime):
	ogDatetime=datetime.datetime.strptime(ogDatetime, "%Y-%m-%d %H:%M:%S")
	epochTime = ogDatetime.strftime('%s')

	return epochTime
