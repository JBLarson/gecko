#!/usr/bin/python3

from time import strftime, strptime, localtime
#from datetime import datetime, strftime, strptime
from datetime import datetime, timedelta
import json
import dateparser
import math



# import symbolName data
symbolNamesInAddr = 'data/allSymbols.json'

with open(symbolNamesInAddr, 'r') as r:
	symbolNameDict = json.load(r)

symbolNames = list(symbolNameDict.values())
symbolIds = list(symbolNameDict.keys())

#print(symbolIds)



dtNowOG = datetime.now()
dtNowOGsplit = str(dtNowOG).split('.')
dtNow = dtNowOGsplit[0]




def unixToDatetime(epochTime):
	localTime = strftime('%Y-%m-%d', localtime(epochTime))

	return localTime


def dtToUnix(ogDatetime):
	ogDatetime = str(ogDatetime)
	ogDt = datetime.strptime(ogDatetime, "%Y-%m-%d %H:%M:%S")
	unixTime = ogDt.strftime('%s')
	return unixTime



def oneYearAgo(ogDatetime):
	inputTypeStr = str(type(ogDatetime))
	if 'str' in inputTypeStr:
		ogDatetime = dateparser.parse(ogDatetime)

	dtOneYearAgo = ogDatetime - timedelta(days=365)
	return dtOneYearAgo


oneYearAgoDate = oneYearAgo(dtNow)



todayUnix = dtToUnix(dtNow)
oneYearAgoUnix = dtToUnix(oneYearAgoDate)



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


geckoData = {}
#for symbolId in symbolIds[0:1]:
for symbolId in symbolIds[0:50]:
	getCoin = getCoinDict(symbolId, 'usd', oneYearAgoUnix, todayUnix)
	resultBase = getCoin['base']
	resultQuote = getCoin['quote']
	resultPair = resultQuote + '/' + resultBase
	print("Fetched data for: " + resultPair)
	resultDict = {resultPair: getCoin}
	geckoData.update(resultDict)


#print(geckoData)
#print(getCoinTest)




def createJsonFunc(jsonOutAddr, jsonData):
	try:
		with open(jsonOutAddr, 'w') as fp1: json.dump(jsonData, fp1)
		functionOutput = ("\nSuccess Creating JSON at: " + str(jsonOutAddr) + "\n")

	except Exception as e:
		functionOutput = "\nFailed to create JSON. Error msg:\n" + str(e)

	return functionOutput



# save data to json file
writeGeckoData = createJsonFunc('data/bigGecko.json', geckoData)
print(writeGeckoData)
