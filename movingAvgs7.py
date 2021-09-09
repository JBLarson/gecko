#!/usr/bin/python3

from geckoFuncz import thirtyDayFunc, dataFor30Func, analyzeTokenFunc, stdDevFunc2
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
print("\nStarted 7-day SMA Script on: " + str(justDate) + " at: " + str(justTime) + "\n")



# import gecko analysis data
jsonInAddr = 'data/geckoAnalysis2.json'

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




def dataForNFunc(dataSet, centerDate):
	nDayList = nDayFunc(centerDate, 50)
	dictNDays = {}
	dateKeys = list(dataSet.keys())
	for dateKey in dateKeys:
		if dateKey in thirtyDayList:
			currentPrice = dataSet[dateKey]		
			currentPriceDict = {dateKey: currentPrice}
			dictNDays.update(currentPriceDict)
	return dictNDays



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
	currentMovingAvg7Dict = createMovingAvgDict(geckoKey, 7)

	currentGeckoData = geckoData[geckoKey]
	currentGeckoData['movingAvg7'] = currentMovingAvg7Dict

	print("Added 7-day SMA for: " + str(currentGeckoData['pair']))



time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nCompleted sort on: " + str(justDate) + " at: " + str(justTime) + "\n")




jsonOutAddr = 'data/geckoAnalysis3.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(geckoData, fp1)

	print("\nSuccess Creating Sorted Trade JSON file at: " + str(jsonOutAddr) + '\n')


except Exception as e: print(e)




