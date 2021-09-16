#!/usr/bin/python3

import time
import datetime
import json
from geckoFuncz import unixToDatetime, datetimeToUnix, analyzeAllTokens, stdDevFunc, pChangeFunc


# import symbolName data
symbolNamesInAddr = 'data/symbolNames.json'

with open(symbolNamesInAddr, 'r') as r:
	symbolNameDict = json.load(r)




def oneYearAgo(ogDT):
	splitDT = ogDT.split("-")
	year = splitDT[0]
	
	restOfDt = str(splitDT[1]) +"-" + str(splitDT[2])
	yearMinusOne = int(year) - 1
	oneYearResult = str(yearMinusOne) + "-" + str(restOfDt)
	
	return oneYearResult


today = datetime.datetime.now()
today = str(today).split(".")
today = today[0]
oneYearAgo = oneYearAgo(today)

epochToday = datetimeToUnix(today)
epochOneYearAgo = datetimeToUnix(oneYearAgo)



def getCoinDict(coin, baseCurrency, fromTimeStamp, toTimestamp):
	from pycoingecko import CoinGeckoAPI
	cg = CoinGeckoAPI()

	coinApiRez = cg.get_coin_market_chart_range_by_id(id=coin, vs_currency=baseCurrency, from_timestamp=fromTimeStamp, to_timestamp=toTimestamp) # coin gecko coinApiRez
	coinRezPrices = coinApiRez['prices']
	coinRezVolumes = coinApiRez['total_volumes']

	volumeDict, priceDict = {}, {}
	for price in coinRezPrices:
		priceIndex = coinRezPrices.index(price)
		unixTime = price[0]
		volume = coinRezVolumes[priceIndex][1]
		unixTime = int(str(unixTime)[:-3])
		price = price[1]
		localDT = unixToDatetime(unixTime)

		priceDict.update({localDT: price})
		volumeDict.update({localDT: volume})

	returnDict = {"base": baseCurrency, "quote": coin, "data": priceDict, "volumeData": volumeDict}

	return returnDict



def fetchTokenData(tokenName):
	#tokenName = symbolNameFunc(tokenSymbol)
	tokenName = tokenName.lower()
	tokenUsd, tokenEur = getCoinDict(tokenName, 'usd', epochOneYearAgo, epochToday), getCoinDict(tokenName, 'eur', epochOneYearAgo, epochToday)
	tokenUsdEur = [tokenUsd, tokenEur]
	return tokenUsdEur



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

geckoData = getAllTokens(symbolNameDict)

geckoKeys = list(geckoData.keys())



# create sample stats for each token
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




# find stdDeviation for each token
for geckoKey in geckoKeys:
	currentGdict = geckoData[geckoKey]
	stdDev = stdDevFunc(currentGdict)
	currentGdict.update({'stdDev': stdDev})



# find daily percentage change for each token
for geckoKey in geckoKeys:
	currentTokenDict = geckoData[geckoKey]
	pChangeDict = pChangeFunc(currentTokenDict)
	currentTokenDict['pChange'] = pChangeDict



jsonOutAddr = 'data/geckoAnalysis' + '.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(geckoData, fp1)


	print("\nSuccess Creating Crypto Json on/at: " + str(jsonOutAddr) + "\n")

except Exception as e:
	print(e)

