#!/usr/bin/python3

from geckoFuncz import thirtyDayFunc, dataFor30Func, analyzeTokenFunc, stdDevFunc2
import json
import math
import dateparser
from datetime import datetime, timedelta, date
from time import strftime

#lambda functions for rounding
ro1, ro2, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 6), lambda x : round(x, 8)


time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nStarted sort on: " + str(justDate) + " at: " + str(justTime) + "\n")



# import coinGecko data
jsonInAddr = 'data/OGgecko.json'

with open(jsonInAddr, 'r') as f:
	geckoData = json.load(f)

geckoKeys = list(geckoData.keys())


def percentChange(fromNum, toNum):
	pChange = ((toNum - fromNum)/fromNum)*100
	return pChange


# function that returns 52W-high
def listMaxFunc(targetDict):
	firstKey = (list(targetDict.keys()))[0]
	maxItem = {firstKey: targetDict[firstKey]}
	targetKeys = targetDict.keys()
	for targetKey in targetKeys:
		maxDate = list(maxItem.keys())[0]
		if targetDict[targetKey] > maxItem[maxDate]:
			maxItem = {targetKey: targetDict[targetKey]}
	return maxItem


# function that returns 52W-low
def listMinFunc(targetDict):
	firstKey = (list(targetDict.keys()))[0]
	minItem = {firstKey: targetDict[firstKey]}
	targetKeys = targetDict.keys()
	for targetKey in targetKeys:
		minDate = list(minItem.keys())[0]
		if targetDict[targetKey] < minItem[minDate]:
			minItem = {targetKey: targetDict[targetKey]}
	return minItem


# function that returns 52W avg price
def listAvgFunc(targetDict):
	targetList = list(targetDict.values())
	sumOfRates = 0
	for rate in targetList:
		sumOfRates += rate

	avgRate = sumOfRates / len(targetList)
	return avgRate



# function to run analysis function on all pairs in gecko dictionary
def analyzeAllTokens(geckoData):
	analysisList = []

	quoteKeys = list(geckoData.keys())

	for quoteKey in quoteKeys:
		pairDict = geckoData[quoteKey]
		analyzePair = analyzeTokenFunc(pairDict)
		analysisList.append(analyzePair)
	return analysisList

analyzeAll = analyzeAllTokens(geckoData)

for aDict in analyzeAll:
	aDictPair = aDict['pair']
	
	baseKeys = geckoData.keys()
	for baseKey in baseKeys:
		currentGeckoDict = geckoData[baseKey]
		currentGekkoQuote = currentGeckoDict['quote']
		currentGekkoBase = currentGeckoDict['base']
		currentGekkoPair = str(currentGekkoQuote).capitalize() + str(currentGekkoBase).capitalize()
		if aDictPair == currentGekkoPair:
			currentGeckoDict.update(aDict)





def stdDevFunc(currentGeckoDict):
	currentPriceData = currentGeckoDict['data']
	currentAvg = currentGeckoDict['avg']
	currentMeanDevSquaredSum = 0
	for currentDate in currentPriceData:
		currentPrice = currentPriceData[currentDate]
		currentMeanDeviation = currentPrice - currentAvg
		currentMeanDevSquaredSum += currentMeanDeviation * currentMeanDeviation
	currentVariance = currentMeanDevSquaredSum / len(currentPriceData)
	currentStdDev = math.sqrt(currentVariance)
	return currentStdDev

for geckoKey in geckoKeys:
	currentGdict = geckoData[geckoKey]
	stdDev = stdDevFunc(currentGdict)
	currentGdict.update({'stdDev': stdDev})




def dataFor30Func(dataSet, centerDate):
	thirtyDayList = thirtyDayFunc(centerDate)
	analysisDict = {}
	dateKeys = list(dataSet.keys())
	for dateKey in dateKeys:
		if dateKey in thirtyDayList:
			currentPrice = dataSet[dateKey]		
			currentPriceDict = {dateKey: currentPrice}
			analysisDict.update(currentPriceDict)
	
	dataAvgPrice = listAvgFunc(analysisDict)
	dataMinPrice = listMinFunc(analysisDict)
	dataMaxPrice = listMaxFunc(analysisDict)
	dataStdDev = stdDevFunc2(analysisDict)
	listAnalysis = {'stdDev': dataStdDev, 'avg': dataAvgPrice, 'max': dataMaxPrice, 'min': dataMinPrice}

	outputDict = {centerDate: listAnalysis}

	return outputDict




def thirtyDayFunc(ogDt):
	thirtyDayList = []

	thirtyDayList.append(ogDt)


	for dayCounter in range(15):
		dayCounter = dayCounter+1
		dtDt = dateparser.parse(ogDt)
		addDaysFull = dtDt + timedelta(days = dayCounter)

		subtractDaysFull = dtDt - timedelta(days = dayCounter)

		addDaysSplit = str(addDaysFull).split(" ")
		subtractDaysSplit = str(subtractDaysFull).split(" ")
		addDays = addDaysSplit[0]
		subtractDays = subtractDaysSplit[0]
		thirtyDayList.append(addDays)
		thirtyDayList.append(subtractDays)
	thirtyDayList.sort(reverse=False)

	return thirtyDayList


def dataFor30Func(dataSet, centerDate):
	thirtyDayList = thirtyDayFunc(centerDate)
	dict30Days = {}
	dateKeys = list(dataSet.keys())
	for dateKey in dateKeys:
		if dateKey in thirtyDayList:
			currentPrice = dataSet[dateKey]		
			currentPriceDict = {dateKey: currentPrice}
			dict30Days.update(currentPriceDict)
	return dict30Days



def movingAvgFunc(dataSet, centerDate):
	thirtyDayList = thirtyDayFunc(centerDate)
	analysisDict = {}
	dateKeys = list(dataSet.keys())
	for dateKey in dateKeys:
		if dateKey in thirtyDayList:
			currentPrice = dataSet[dateKey]		
			currentPriceDict = {dateKey: currentPrice}
			analysisDict.update(currentPriceDict)
	
	dataAvgPrice = listAvgFunc(analysisDict)
	movingAvgDict = {centerDate: dataAvgPrice}

	return movingAvgDict


def createMovingAvgDict(tokenPair):
	tokenData = geckoData[tokenPair]['data']

	movingAvgDict = {}
	for date in tokenData:
		movingAvg30 = movingAvgFunc(tokenData, date)

		movingAvgDict.update(movingAvg30)


	return movingAvgDict


for geckoKey in geckoKeys:
	currentMovingAvg30Dict = createMovingAvgDict(geckoKey)
	currentGeckoData = geckoData[geckoKey]
	currentGeckoData['movingAvg30'] = currentMovingAvg30Dict
#print(adaMovingAvg30Dict)

#print(geckoData['AdaUsd'])

"""for date in adaData:
	movingAvg30 = movingAvgFunc(adaData, date)

	print("\n")
	print(movingAvg30)
"""


time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nCompleted sort on: " + str(justDate) + " at: " + str(justTime) + "\n")




jsonOutAddr = 'data/geckoAnalysis.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(geckoData, fp1)

	print("\nSuccess Creating Sorted Trade JSON file at: " + str(jsonOutAddr) + '\n')


except Exception as e: print(e)




