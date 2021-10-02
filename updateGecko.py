
from datetime import datetime
from time import strftime
import dateparser
import json
from geckoFuncz import *
import pycoingecko
from ezDT import *



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


	echoDtOutput = echoDt('Started', "Price Update")


	# datetime / epoch variables
	today = datetime.datetime.now()
	today = str(today).split(".")
	today = today[0]
	todaySplit = str(today).split(" ")
	todayYmd = todaySplit[0]
	unixToday = datetimeToUnix(today)
	dateOneYearAgo = subtractDays(today, 365)
	unixOneYearAgo = datetimeToUnix(str(dateOneYearAgo))




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


	echoDtOutput = echoDt('Completed', "Price Update")

	echoDtOutput = echoDt('Started', "Sample Stats")





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



	echoDtOutput = echoDt('Completed', "Sample Stats")



	jsonOutAddr = 'data/geckoUpdate' + '.json'
	try:
		with open(jsonOutAddr, 'w') as fp1: json.dump(geckoData, fp1)
		print("\nSuccess Creating Crypto Json on/at: " + str(jsonOutAddr) + "\n")

	except Exception as e:
		print(e)


elif upToDate == True:
	print("\nPrice Data is current\n")
