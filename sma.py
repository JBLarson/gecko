#!/usr/bin/python3

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
print("\nStarted SMA Script on: " + str(justDate) + " at: " + str(justTime) + "\n")



# import gecko analysis data
jsonInAddr = 'data/geckoAnalysis.json'

with open(jsonInAddr, 'r') as f:
	geckoData = json.load(f)

geckoKeys = list(geckoData.keys())


# function that returns 52W avg price
def listAvgFunc(targetDict):
	targetList = list(targetDict.values())
	sumOfRates = 0
	for rate in targetList:
		sumOfRates += rate

	avgRate = sumOfRates / len(targetList)
	return avgRate




def nDayFunc(ogDt, n):
	nDayList = []
	n = n - 1
	nDayList.append(ogDt)

	halfN = n / 2

	for dayCounter in np.arange(halfN):
		dtDt = dateparser.parse(ogDt)

		dayCounter = dayCounter+1
		addDaysFull = dtDt + timedelta(days = dayCounter)
		subtractDaysFull = dtDt - timedelta(days = dayCounter)

		addDaysSplit = str(addDaysFull).split(" ")
		subtractDaysSplit = str(subtractDaysFull).split(" ")
		addDays = addDaysSplit[0]
		subtractDays = subtractDaysSplit[0]
		nDayList.append(addDays)
		nDayList.append(subtractDays)
	nDayList.sort(reverse=False)
	nDayList.pop()
	return nDayList




def movingAvgFunc(dataSet, centerDate, n):
	nDayList = nDayFunc(centerDate, n)
	analysisDict = {}
	dateKeys = list(dataSet.keys())
	for dateKey in dateKeys:
		if dateKey in nDayList:
			currentPrice = dataSet[dateKey]		
			currentPriceDict = {dateKey: currentPrice}
			analysisDict.update(currentPriceDict)
	
	dataAvgPrice = listAvgFunc(analysisDict)
	movingAvgDict = {centerDate: dataAvgPrice}

	return movingAvgDict


def createMovingAvgDict(tokenPair, n):
	tokenData = geckoData[tokenPair]['data']

	movingAvgDict = {}
	for date in tokenData:
		movingAvgN = movingAvgFunc(tokenData, date, n)

		movingAvgDict.update(movingAvgN)


	return movingAvgDict


for geckoKey in geckoKeys:
	# calculate SMA
	currentMovingAvg7Dict = createMovingAvgDict(geckoKey, 7)
	currentMovingAvg14Dict = createMovingAvgDict(geckoKey, 14)
	currentMovingAvg30Dict = createMovingAvgDict(geckoKey, 30)
	currentMovingAvg50Dict = createMovingAvgDict(geckoKey, 50)
	currentMovingAvg200Dict = createMovingAvgDict(geckoKey, 200)
	currentGeckoData = geckoData[geckoKey]
	
	# add SMA's to dictionary
	currentGeckoData['movingAvg7'] = currentMovingAvg7Dict

	print("Added 7-day SMA for: " + str(currentGeckoData['pair']))

	currentGeckoData['movingAvg14'] = currentMovingAvg14Dict

	print("Added 14-day SMA for: " + str(currentGeckoData['pair']))

	currentGeckoData['movingAvg30'] = currentMovingAvg30Dict

	print("Added 30-day SMA for: " + str(currentGeckoData['pair']))

	currentGeckoData['movingAvg50'] = currentMovingAvg50Dict

	print("Added 50-day SMA for: " + str(currentGeckoData['pair']))

	currentGeckoData['movingAvg200'] = currentMovingAvg200Dict

	print("Added 200-day SMA for: " + str(currentGeckoData['pair']))


time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nCompleted SMA script on: " + str(justDate) + " at: " + str(justTime) + "\n")




jsonOutAddr = 'data/geckoAnalysis2.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(geckoData, fp1)

	print("\nSuccess Processing SMA's - JSON output file at: " + str(jsonOutAddr) + '\n')


except Exception as e: print(e)




