
import time
import datetime
import json
import dateparser
import math

def unixToDatetime(epochTime):
	localTime = time.strftime('%Y-%m-%d', time.localtime(epochTime))

	return localTime



def datetimeToUnix(ogDatetime):
	ogDatetime=datetime.datetime.strptime(ogDatetime, "%Y-%m-%d %H:%M:%S")
	epochTime = ogDatetime.strftime('%s')

	return epochTime




def thirtyDayFunc(ogDt):
	thirtyDayList = []

	thirtyDayList.append(ogDt)


	for dayCounter in range(15):
		dayCounter = dayCounter+1
		dtDt = dateparser.parse(ogDt)
		addDaysFull = dtDt + datetime.timedelta(days = dayCounter)

		subtractDaysFull = dtDt - datetime.timedelta(days = dayCounter)

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





# function that returns high price in price dict
def maxFunc(targetDict):
	firstKey = (list(targetDict.keys()))[0]
	maxItem = {firstKey: targetDict[firstKey]}
	targetKeys = targetDict.keys()
	for targetKey in targetKeys:
		maxDate = list(maxItem.keys())[0]
		if targetDict[targetKey] > maxItem[maxDate]:
			maxItem = {targetKey: targetDict[targetKey]}
	return maxItem




# function that returns low price in price dict
def minFunc(targetDict):
	firstKey = (list(targetDict.keys()))[0]
	minItem = {firstKey: targetDict[firstKey]}
	targetKeys = targetDict.keys()
	for targetKey in targetKeys:
		minDate = list(minItem.keys())[0]
		if targetDict[targetKey] < minItem[minDate]:
			minItem = {targetKey: targetDict[targetKey]}
	return minItem





# function that returns avg price for priceDict
def avgFunc(targetDict):
	targetList = list(targetDict.values())
	sumOfRates = 0
	for rate in targetList:
		sumOfRates += rate

	avgRate = sumOfRates / len(targetList)
	return avgRate



def stdDevFunc2(currentPriceData):
	currentAvg = avgFunc(currentPriceData)
	currentMeanDevSquaredSum = 0
	for currentDate in currentPriceData:
		currentPrice = currentPriceData[currentDate]
		currentMeanDeviation = currentPrice - currentAvg
		currentMeanDevSquaredSum += currentMeanDeviation * currentMeanDeviation
	currentVariance = currentMeanDevSquaredSum / len(currentPriceData)
	currentStdDev = math.sqrt(currentVariance)
	return currentStdDev



# function that returns avg, 52W-low, and 52W-high
def analyzeTokenFunc(targetDict):
	#targetDict = geckoData[targetBase.lower()][targetPair]['data']
	targetQuote, targetBase = targetDict['quote'], targetDict['base']
	targetDictList = targetDict['data']
	targetPair = str(targetQuote).capitalize() + str(targetBase).capitalize()
	listAvgPrice = avgFunc(targetDictList)
	listMinPrice = minFunc(targetDictList)
	listMaxPrice = maxFunc(targetDictList)
	listAnalysis = {'pair': targetPair, 'avg': listAvgPrice, 'max': listMaxPrice, 'min': listMinPrice}

	return listAnalysis

