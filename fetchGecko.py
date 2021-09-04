#!/usr/bin/python3

import time
import datetime
import requests
import json
from geckoFuncz import unixToDatetime, datetimeToUnix


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
	priceDict = {}
	for price in coinRezPrices:
		
		unixTime = price[0]
		unixTime = int(str(unixTime)[:-3])
		price = price[1]
		localDT = unixToDatetime(unixTime)

		priceDict.update({localDT: price})

	returnDict = {"base": baseCurrency, "quote": coin, "data": priceDict}

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

allTokens = getAllTokens(symbolNameDict)



jsonOutAddr = 'data/OGgecko' + '.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(allTokens, fp1)


	print("\nSuccess Creating Crypto Json on/at: " + str(jsonOutAddr) + "\n")

except Exception as e:
	print(e)
