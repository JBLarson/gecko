
from datetime import datetime
from time import strftime
import dateparser
import json
from geckoFuncz import unixToDatetime, datetimeToUnix, analyzeTokenFunc, stdDevFunc, upToDateFunc
import pycoingecko


try:
	jsonInAddr = 'data/geckoUpdate' + '.json'
	with open(jsonInAddr, 'r') as f:
		geckoData = json.load(f)

except:
	# import coinGecko data
	jsonInAddr = 'data/geckoAnalysis.json'

	with open(jsonInAddr, 'r') as f:
		geckoData = json.load(f)

geckoKeys = list(geckoData.keys())




upToDate = upToDateFunc(geckoData)


if upToDate == False:

	time = datetime.now()
	dtRn = str(strftime("%x") + " " + strftime("%X"))
	justTime, justDate = strftime("%X"), strftime("%x")
	print("\nStarted Update on: " + str(justDate) + " at: " + str(justTime) + "\n")




	# datetime / epoch variables
	today = datetime.now()
	today = str(today).split(".")
	today = today[0]
	todaySplit = str(today).split(" ")
	todayYmd = todaySplit[0]
	unixToday = datetimeToUnix(today)



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




	def updateGeckoData(currentGeckoDict):
		currentBase = currentGeckoDict['base']
		currentQuote = currentGeckoDict['quote']
		currentPair = currentQuote + "/" + currentBase
		currentGeckoPriceData = currentGeckoDict['data']
		currentGeckoVolumeData = currentGeckoDict['volumeData']

		currentDates = list(currentGeckoPriceData.keys())
		currentDates.sort(reverse=False)
		lastDate = currentDates[-1]
		if lastDate < todayYmd:
			unixLastDate = datetimeToUnix(lastDate)
			updateData = getCoinDict(currentQuote, currentBase, unixLastDate, unixToday)
			updatedPriceData = updateData['data']
			updatedVolumeData = updateData['volumeData']

			currentGeckoPriceData.update(updatedPriceData)
			currentGeckoVolumeData.update(updatedVolumeData)
			updateFuncOutput = currentPair + " has been updated"

		else:
			updateFuncOutput = currentPair + " is up to date"

		return updateFuncOutput


	for geckoKey in geckoKeys:
		currentGeckoData = geckoData[geckoKey]
		updateData = updateGeckoData(currentGeckoData)
		print(updateData)


	time = datetime.now()
	dtRn = str(strftime("%x") + " " + strftime("%X"))
	justTime, justDate = strftime("%X"), strftime("%x")
	print("\nCompleted Update on: " + str(justDate) + " at: " + str(justTime) + "\n")


	time = datetime.now()
	dtRn = str(strftime("%x") + " " + strftime("%X"))
	justTime, justDate = strftime("%X"), strftime("%x")
	print("\nStarted sampleStats on: " + str(justDate) + " at: " + str(justTime) + "\n")






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




	for geckoKey in geckoKeys:
		currentGdict = geckoData[geckoKey]
		currentPriceDict = currentGdict['data']
		stdDev = stdDevFunc(currentPriceDict)
		currentGdict.update({'stdDev': stdDev})



	time = datetime.now()
	dtRn = str(strftime("%x") + " " + strftime("%X"))
	justTime, justDate = strftime("%X"), strftime("%x")
	print("\nCompleted sample stats on: " + str(justDate) + " at: " + str(justTime) + "\n")



	jsonOutAddr = 'data/geckoUpdate' + '.json'
	try:
		with open(jsonOutAddr, 'w') as fp1: json.dump(geckoData, fp1)
		print("\nSuccess Creating Crypto Json on/at: " + str(jsonOutAddr) + "\n")

	except Exception as e:
		print(e)


elif upToDate == True:
	print("\nPrice Data is current\n")
