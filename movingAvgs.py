#!/usr/bin/python3

from geckoFuncz import *
import json
import math
import dateparser
from datetime import datetime, timedelta, date
from time import strftime
import numpy as np
#lambda functions for rounding
ro1, ro2, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 6), lambda x : round(x, 8)


time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nStarted 7-day, 30-day, 50-day & 200-day SMA Script on: " + str(justDate) + " at: " + str(justTime) + "\n")



# import gecko analysis data
jsonInAddr = 'data/geckoAnalysis.json'

with open(jsonInAddr, 'r') as f:
	geckoData = json.load(f)

geckoKeys = list(geckoData.keys())


def createMovingAvgDict(tokenPair, n):
	tokenData = geckoData[tokenPair]['data']

	movingAvgDict = {}
	for date in tokenData:
		movingAvgN = movingAvgFunc(tokenData, date, n)
		movingAvgDict.update(movingAvgN)

	return movingAvgDict


for geckoKey in geckoKeys:

	currentGeckoData = geckoData[geckoKey]


	# added more text output bc this script is slow as balls
	currentMovingAvg7Dict = createMovingAvgDict(geckoKey, 7)
	print("Added 7-day SMA for: " + str(currentGeckoData['pair']))
	currentMovingAvg30Dict = createMovingAvgDict(geckoKey, 30)
	print("Added 30-day SMA for: " + str(currentGeckoData['pair']))
	currentMovingAvg50Dict = createMovingAvgDict(geckoKey, 50)
	print("Added 50-day SMA for: " + str(currentGeckoData['pair']))
	currentMovingAvg200Dict = createMovingAvgDict(geckoKey, 200)
	print("Added 200-day SMA for: " + str(currentGeckoData['pair']))



	currentGeckoData['movingAvg7'] = currentMovingAvg7Dict
	currentGeckoData['movingAvg30'] = currentMovingAvg30Dict
	currentGeckoData['movingAvg50'] = currentMovingAvg50Dict
	currentGeckoData['movingAvg200'] = currentMovingAvg200Dict



time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nCompleted sort on: " + str(justDate) + " at: " + str(justTime) + "\n")




jsonOutAddr = 'data/geckoAnalysis2.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(geckoData, fp1)

	print("\nSuccess Creating Sorted Trade JSON file at: " + str(jsonOutAddr) + '\n')


except Exception as e: print(e)




