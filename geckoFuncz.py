
from time import *
from datetime import *
import time
import json
import dateparser
import math
import numpy as np





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










# ---
# for api request part of fetchGecko
# ---


# convert a unix epoch value to YYYY-MM-DD
def epochToDatetime(epochTime):
	localTime = time.strftime('%Y-%m-%d', time.localtime(epochTime))

	return localTime



# get data from the coingecko API using a coin's symbol and a base fiat currency

def getCoinDict(coin, baseCurrency):
	from pycoingecko import CoinGeckoAPI
	cg = CoinGeckoAPI()

	coinApiRez = cg.get_coin_market_chart_by_id(id=coin,vs_currency=baseCurrency,days='365')

	coinRezPrices = coinApiRez['prices']
	coinRezVolumes = coinApiRez['total_volumes']

	volumeDict, priceDict = {}, {}
	for price in coinRezPrices:
		priceIndex = coinRezPrices.index(price)
		unixTime = price[0]
		volume = coinRezVolumes[priceIndex][1]
		unixTime = int(str(unixTime)[:-3])
		price = price[1]
		localDT = epochToDatetime(unixTime)

		priceDict.update({localDT: price})
		volumeDict.update({localDT: volume})

	returnDict = {"base": baseCurrency, "quote": coin, "data": priceDict, "volumeData": volumeDict}

	return returnDict



# potentially unneccessary function to call the previous function
# was useful for when this supported multiple base currencies

def fetchTokenData(tokenName):
	#tokenName = symbolNameFunc(tokenSymbol)
	tokenName = tokenName.lower()
	tokenUsd = getCoinDict(tokenName, 'usd')
	tokenUsd = [tokenUsd]
	return tokenUsd



# get all the tokens in the data/symbolNames.json file
def getAllTokens(symbolNameDict):
	tokenDataDict = {}
	symbols = list(symbolNameDict.keys())

	for symbol in symbols:
		symbolName = symbolNameDict[symbol]
		symbolDataList = fetchTokenData(symbolName)
		for symbolData in symbolDataList:	
			symbolBase = symbolData['base']
			pair = str(symbol).capitalize() + str(symbolBase).capitalize()
			tokenDataDict.update({pair: symbolData})

	return tokenDataDict


# ---
# for sample stats part of fetchGecko
# ---


# return the percent change between two numbers
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



# function that returns avg, 52W-low, and 52W-high
def analyzeTokenFunc(targetDict):
	#targetDict = geckoData[targetBase.lower()][targetPair]['data']
	targetQuote, targetBase = targetDict['quote'], targetDict['base']
	targetDictList = targetDict['data']
	targetPair = str(targetQuote).capitalize() + str(targetBase).capitalize()
	listAvgPrice = listAvgFunc(targetDictList)
	listMinPrice = listMinFunc(targetDictList)
	listMaxPrice = listMaxFunc(targetDictList)
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





# ---
# for finding simple moving avgs in movingAvgs.py
# ---



def nDayFunc(ogDt, n):
	nDayList = []
	n = n - 1
	nDayList.append(ogDt)

	halfN = n / 2

	for dayCounter in np.arange(halfN):
		dtDt = dateparser.parse(ogDt, settings={'TIMEZONE': 'UTC'})

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

