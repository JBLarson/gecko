#!/usr/bin/python3

import json
import math
import dateparser
from datetime import datetime, timedelta, date
from time import strftime
import numpy as np
from geckoFuncz import nDayFunc, listAvgFunc, upToDateFunc


# lambda functions for rounding
ro1, ro2, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 6), lambda x : round(x, 8)


time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nStarted SMA Script on: " + str(justDate) + " at: " + str(justTime) + "\n")




# import existing gecko data w/ SMA
existingSMAjsonInAddr = 'data/gAnalysis2.json'

with open(existingSMAjsonInAddr, 'r') as f:
	geckoData = json.load(f)



# import updated gecko price data
priceUpdatejsonInAddr = 'data/geckoAnalysisTest.json'

with open(priceUpdatejsonInAddr, 'r') as f:
	updatedGeckoData = json.load(f)




geckoKeys = list(geckoData.keys())




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






# function for creating a sorted list of dates in a dictionary
def dictDateFunc(targetDict, dictKey):
	dictDates = list(targetDict[dictKey])
	dictDates.sort(reverse=False)
	return dictDates



# functions for updating SMA


def updateMovingAvgDict(tokenPair, n):
	tokenDict = geckoData[tokenPair]
	updatedPriceTokenDict = updatedGeckoData[tokenPair]

	print("Existing SMA Dictionary keys: " + str(tokenDict.keys()))
	print("updated price Dictionary keys: " + str(updatedPriceTokenDict.keys()))

	tokenData = tokenDict['data']
	updateTokenData = updatedPriceTokenDict['data']
	existingPriceDates = dictDateFunc(tokenDict, 'data')
	lastPriceDate = existingPriceDates[-1]
	print("\nExisting data w / SMA")
	print("Last price: " + str(lastPriceDate))

	print("\nUpdated data")
	updatedPriceDates = dictDateFunc(updatedPriceTokenDict, 'data')
	lastUpdatedPriceDate = updatedPriceDates[-1]
	print("Last price: " + str(lastUpdatedPriceDate))

	# need to make function to iterate through moving avgs

	#currentMovingAvg7Dict = tokenDict['movingAvg7']



	allMovingAvgUpdates = {}

	movingAvgLengths = [7, 14, 30, 50, 200]
	for movingAvgLength in movingAvgLengths:
		#print("\nMoving avg update for: " + str(movingAvgLength) + " day SMA")
		currentMovingAvgUpdates = []

		for date in updatedPriceDates:
			if date not in existingPriceDates:


				movingAvgUpdate = movingAvgFunc(updateTokenData, date, movingAvgLength)
				#print(movingAvgUpdate)
				currentMovingAvgUpdates.append(movingAvgUpdate)
		#print(currentMovingAvgUpdates)
		allMovingAvgUpdates.update({movingAvgLength: currentMovingAvgUpdates})
	return allMovingAvgUpdates


#tokenSMA7dates = dictDatesFunc(tokenDict, '')

"""
currentMovingAvgKey = 'movingAvg' + str(n)
currentMovingAvgDict = tokenDict[currentMovingAvgKey]

print(currentMovingAvgDict)
print("\nPrice data: ")
print(tokenData)
"""
"""
movingAvgDict = {}
for date in tokenData:
	movingAvgN = movingAvgFunc(tokenData, date, n)

	movingAvgDict.update(movingAvgN)


return movingAvgDict
"""


updateMovingAvgTest = updateMovingAvgDict('AdaUsd', 30)
print("\nSMA update Data")
print(updateMovingAvgTest)





"""


upToDateResult = upToDateFunc(geckoData)

print(upToDateResult)


print("\nOG update code:\n")

for geckoKey in geckoKeys[0:1]:
	# dictionary for current token
	currentGeckoData = geckoData[geckoKey]



	# calculate SMA
	currentMovingAvg7Dict = createMovingAvgDict(geckoKey, 7)
	#currentMovingAvg14Dict = createMovingAvgDict(geckoKey, 14)
	#currentMovingAvg30Dict = createMovingAvgDict(geckoKey, 30)
	#currentMovingAvg50Dict = createMovingAvgDict(geckoKey, 50)
	#currentMovingAvg200Dict = createMovingAvgDict(geckoKey, 200)
	
	# add SMA's to dictionary
	currentGeckoData['movingAvg7'] = currentMovingAvg7Dict

	print("Added 7-day SMA for: " + str(currentGeckoData['pair']))
	
	currentGeckoData['movingAvg14'] = currentMovingAvg14Dict

	print("Added 14-day SMA for: " + str(currentGeckoData['pair']))

	currentGeckoData['movingAvg30'] = currentMovingAvg30Dict

	print("Added 30-day SMA for: " + str(currentGeckoData['pair']))

	currentGeckoData['movingAvg50'] = currentMovingAvg50Dict

	print("Added 50-day SMA for: " + str(currentGeckoData['pair']))

	currentGeckoData['movingAvg200'] = currentMovingAvg200Dict

	print("Added 200-day SMA for: " + str(currentGeckoData['pair']))
	

time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nCompleted SMA script on: " + str(justDate) + " at: " + str(justTime) + "\n")






jsonOutAddr = 'data/geckoAnalysis2.json'

jsonOutAddr = 'data/geckoAnalysis2Test.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(geckoData, fp1)

	print("\nSuccess Processing SMA's - JSON output file at: " + str(jsonOutAddr) + '\n')


except Exception as e: print(e)

"""
