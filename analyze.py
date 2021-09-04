#!/usr/bin/python3


import json

# import coinGecko data
jsonInAddr = 'data/OGgecko.json'

with open(jsonInAddr, 'r') as f:
	geckoData = json.load(f)


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

analyzeAll = analyzeAllTokens(geckoData)

for aDict in analyzeAll[0:1]:
	aDictPair = aDict['pair']
	
	print("\n\n" + str(aDictPair))
	baseKeys = geckoData.keys()
	for baseKey in baseKeys:
		currentGeckoDict = geckoData[baseKey]
		print(aDict)
		currentGeckoDict.update(aDict)
		#print(currentGeckoDict)
		#print(currentGeckoDict.keys())
print(geckoData['AdaUsd'])
		#[aDictPair]


jsonOutAddr = 'data/geckoAnalysis.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(geckoData, fp1)

	print("\nSuccess Creating Sorted Trade JSON file at: " + str(jsonOutAddr) + '\n')


except Exception as e: print(e)



"""
# function for sorting key
def sortByPair(theDict):
	return theDict['pair']


# function to describe analysis data
def describeAnalysisFunc(analysisDicts):
	for analysisDict in analysisDicts:
		currentPair = analysisDict['pair']
		currentAvg = analysisDict['avg']
		currentLowDate = list(analysisDict['min'].keys())[0]
		currentLow = analysisDict['min'][currentLowDate]
		currentHighDate = list(analysisDict['max'].keys())[0]
		currentHigh = analysisDict['max'][currentHighDate]
		print("\n"+ str(currentPair))
		print("52 Week Avg: " + str(currentAvg))
		print("52 Week High: " + str(currentHigh) + " on: " + str(currentHighDate))
		print("52 Week Low: " + str(currentLow) + " on: " + str(currentLowDate))


analyzeAll = analyzeAllTokens(geckoData)

analyzeAll.sort(key=sortByPair)

def analysisFunc2(analysisDicts):
	for analysisDict in analysisDicts:

		currentPair = analysisDict['pair']
		currentAvg = analysisDict['avg']
		currentLowDate = list(analysisDict['min'].keys())[0]
		currentLow = analysisDict['min'][currentLowDate]
		currentHighDate = list(analysisDict['max'].keys())[0]
		currentHigh = analysisDict['max'][currentHighDate]
		geckoDataEur = geckoData['eur']
		geckoDataUsd = geckoData['usd']

		print("\n\n"+ str(currentPair))
		print("52 Week Avg: " + str(currentAvg))
		print("52 Week High: " + str(currentHigh) + " on: " + str(currentHighDate))
		print("52 Week Low: " + str(currentLow) + " on: " + str(currentLowDate))


		if 'usd' in currentPair.lower():
			currentGeckoData = geckoDataUsd[currentPair]['data']
		if 'eur' in currentPair.lower():
			currentGeckoData = geckoDataEur[currentPair]['data']

		geckoKeys = list(currentGeckoData.keys())
		for key in geckoKeys:
			print(str(key) + " " + str(currentGeckoData[key]))

analysis2 = analysisFunc2(analyzeAll)

print(analysis2)

#describeAnalysis = describeAnalysisFunc(analyzeAll)#


"""
