
from time import strftime, strptime
from datetime import datetime
import json
import dateparser
import math



def unixToDatetime(epochTime):
	localTime = strftime('%Y-%m-%d', time.localtime(epochTime))

	return localTime


def datetimeToUnix(ogDatetime):
	try:	
		try:
			ogDatetime= strptime(ogDatetime, "%Y-%m-%d %H:%M:%S")
		except:
			ogDatetime= strptime(ogDatetime, "%Y-%m-%d")
	except Exception as e:
		print(e)
	epochTime = ogDatetime.strftime('%s')

	return epochTime




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



def stdDevFunc(currentPriceData):
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



# function to run analysis function on all pairs in gecko dictionary
def analyzeAllTokens(geckoData):
	analysisList = []

	quoteKeys = list(geckoData.keys())

	for quoteKey in quoteKeys:
		pairDict = geckoData[quoteKey]
		analyzePair = analyzeTokenFunc(pairDict)
		analysisList.append(analyzePair)
	return analysisList




# use smaUpToDateFunc to determine if SMA's need to be created or updated
# previously called upToDateFunc

def smaUpToDateFunc(geckoData):
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




# use upToDateFunc to determine if price's need to be updated

def upToDateFunc(geckoData):
	# datetime variables
	todayOG = datetime.now()
	todaySplit = str(todayOG).split(" ")
	today = todaySplit[0]

	latestDateList = []

	geckoKeys = list(geckoData.keys())
	for key in geckoKeys:
		currentGeckoData = geckoData[key]
		priceData = currentGeckoData['data']
		priceDates = list(priceData.keys())
		priceDates.sort(reverse=False)
		latestPriceDate = priceDates[-1]
		latestDateList.append(latestPriceDate)

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




def echoDt(scriptStatus, scriptType):
	time = datetime.now()
	dtRn = str(strftime("%x") + " " + strftime("%X"))
	justTime, justDate = strftime("%X"), strftime("%x")
	echoDtOutput = ("\n" + str(scriptStatus) + " " + str(scriptType) + " Script on: " + str(justDate) + " at: " + str(justTime) + "\n")
	print(echoDtOutput)
	return echoDtOutput



def percentChange(fromNum, toNum):
	pChange = ((toNum - fromNum)/fromNum)*100
	return pChange




def pChangeFunc(tokenDict):
	pChangeDict = {}
	tokenPrices = tokenDict['data']
	tokenDates = list(tokenPrices.keys())
	for currentDate in tokenDates:
		dateIndex = tokenDates.index(currentDate)
		currentPrice = tokenPrices[currentDate]
		if dateIndex != 0:
			lastDate = tokenDates[dateIndex-1]
			lastPrice = tokenPrices[lastDate]
			currentPChange = percentChange(lastPrice, currentPrice)
			pChangeDict.update({currentDate: currentPChange})

	return pChangeDict


