
import time
import datetime
import json
import dateparser
import math

def unixToDatetime(epochTime):
	localTime = time.strftime('%Y-%m-%d', time.localtime(epochTime))

	return localTime


def datetimeToUnix(ogDatetime):
	try:	
		try:
			ogDatetime=datetime.datetime.strptime(ogDatetime, "%Y-%m-%d %H:%M:%S")
		except:
			ogDatetime=datetime.datetime.strptime(ogDatetime, "%Y-%m-%d")
	except Exception as e:
		print(e)
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


# use upToDateFunc to determine if SMA's need to be created or updated

def upToDateFunc(geckoData):
	# datetime variables
	todayOG = datetime.now()
	todaySplit = str(todayOG).split(" ")
	today = todaySplit[0]

	latestDateList = []

	geckoKeys = list(geckoData.keys())
	for key in geckoKeys:
		currentGeckoData = geckoData[key]
		movingAvg7Data = currentGeckoData['movingAvg7']
		movingAvg7Dates = list(movingAvg7Data.keys())
		movingAvg7Dates.sort(reverse=False)
		latestMovingAvg7Date = movingAvg7Dates[-1]
		latestDateList.append(latestMovingAvg7Date)

	for date in latestDateList:
		if date == today:
			upToDateOutput = True
		else:
			upToDateOutput = False


	return upToDateOutput


# renamed but keeping original for now to avoid errors
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






def createJsonFunc(jsonOutAddr, jsonData):
	try:
		with open(jsonOutAddr, 'w') as fp1: json.dump(jsonData, fp1)
		functionOutput = ("\nSuccess Creating JSON at: " + str(jsonOutAddr) + "\n")

	except Exception as e:
		functionOutput = "\nFailed to create JSON. Error msg:\n" + str(e)

	return functionOutput




def readJsonFunc(jsonInAddr):
	with open(jsonInAddr, 'r') as r:
		jsonOutputDict = json.load(r)
	return jsonOutputDict


