#!/usr/bin/python3

import time
import datetime
import json
from geckoFuncz import unixToDatetime, datetimeToUnix, analyzeAllTokens, stdDevFunc, pChangeFunc
import ezDT
try:
	from pycoingecko import CoinGeckoAPI
	cg = CoinGeckoAPI()
except:
	print("failed to import coingeckoAPI")


# import symbolName data
symbolNamesInAddr = 'data/allSymbols.json'

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


def lastYearOfDates(todaysDateTime):

	dateList = []

	for i in range(365):
		iDatetime = str(ezDT.subtractDays(todaysDateTime, i))
		iDate = iDatetime.split(" ")[0]
		dateList.append(iDate)

	return dateList



lastYearTest = lastYearOfDates(today)



def readDict(inputDict):
	iDictKeys = list(inputDict.keys())
	for iDictKey in iDictKeys:
		print(str(iDictKey) + " " + str(inputDict[iDictKey]))



def fetchStats(coin, targetDate):
	coinApiRez = cg.get_coin_history_by_id(id=coin, date=targetDate, localization='false') # coin gecko coinApiRez

	print("\n" + str(coinApiRez['market_data'].keys()))
	print("\n")
	communityData = coinApiRez['community_data']
	devData = coinApiRez['developer_data']
	readCommunityData = readDict(communityData)



fetchTest = fetchStats('cardano', '29-10-2021')




"""
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

# find max, min, avg for each token
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
	currentPriceDict = currentGdict['data']
	stdDev = stdDevFunc(currentPriceDict)
	currentGdict.update({'stdDev': stdDev})





# find daily percentage change for each token
for geckoKey in geckoKeys:
	currentTokenDict = geckoData[geckoKey]
	pChangeDict = pChangeFunc(currentTokenDict)
	currentTokenDict['pChange'] = pChangeDict





"""



"""
jsonOutAddr = 'data/analyzeSocial' + '.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(geckoData, fp1)


	print("\nSuccess Creating Crypto Json on/at: " + str(jsonOutAddr) + "\n")

except Exception as e:
	print(e)

"""
