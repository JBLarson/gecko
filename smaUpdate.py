#!/usr/bin/python3

import json
import math
import dateparser
from datetime import datetime, timedelta, date
from time import strftime
import numpy as np
from geckoFuncz import nDayFunc, listAvgFunc, upToDateFunc, createJsonFunc


# lambda functions for rounding
ro1, ro2, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 6), lambda x : round(x, 8)


time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nStarted SMA Script on: " + str(justDate) + " at: " + str(justTime) + "\n")




# import existing gecko data w/ SMA
existingSMAjsonInAddr = 'data/geckoAnalysis2.json'

with open(existingSMAjsonInAddr, 'r') as f:
	geckoData = json.load(f)



# import updated gecko price data
priceUpdatejsonInAddr = 'data/geckoUpdate.json'

with open(priceUpdatejsonInAddr, 'r') as f:
	updatedGeckoData = json.load(f)




geckoKeys = list(geckoData.keys())


# update price data
for geckoKey in geckoKeys:
	currentExistingData = geckoData[geckoKey]
	currentUpdateData = updatedGeckoData[geckoKey]
	existingPriceData = currentExistingData['data']
	updatePriceData = currentUpdateData['data']
	updateKeys, existingKeys = list(updatePriceData.keys()), list(existingPriceData.keys())
	for updateKey in updateKeys:
		if updateKey not in existingKeys:
			existingPriceData.update({updateKey: updatePriceData[updateKey]})
	

# update Volume data
for geckoKey in geckoKeys:
	currentExistingData = geckoData[geckoKey]
	currentUpdateData = updatedGeckoData[geckoKey]
	existingVolumeData = currentExistingData['volumeData']
	updateVolumeData = currentUpdateData['volumeData']
	updateKeys, existingKeys = list(updateVolumeData.keys()), list(existingVolumeData.keys())
	for updateKey in updateKeys:
		if updateKey not in existingKeys:
			existingVolumeData.update({updateKey: updateVolumeData[updateKey]})



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


def updateMovingAvgDict(tokenPair):
	tokenDict = geckoData[tokenPair]
	updatedPriceTokenDict = updatedGeckoData[tokenPair]

	#print("Existing SMA Dictionary keys: " + str(tokenDict.keys()))
	#print("updated price Dictionary keys: " + str(updatedPriceTokenDict.keys()))

	tokenData = tokenDict['data']
	updateTokenData = updatedPriceTokenDict['data']
	existingPriceDates = dictDateFunc(tokenDict, 'data')
	lastPriceDate = existingPriceDates[-1]

	updatedPriceDates = dictDateFunc(updatedPriceTokenDict, 'data')
	lastUpdatedPriceDate = updatedPriceDates[-1]

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


# update SMA data
for geckoKey in geckoKeys:


	currentExistingData = geckoData[geckoKey]
	updatedMovingAvgs = updateMovingAvgDict(geckoKey)




	smaUpdateKeys = list(updatedMovingAvgs.keys())
	for updateKey in smaUpdateKeys:

		smaDictKey = 'movingAvg' + str(updateKey)

		currentUpdate = updatedMovingAvgs[updateKey]
		for updateDict in currentUpdate:
			currentExistingData[smaDictKey].update(updateDict)


updateJson = createJsonFunc('data/geckoAnalysis2.json', geckoData)


time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nCompleted SMA Update on: " + str(justDate) + " at: " + str(justTime) + "\n")
