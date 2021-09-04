#!/usr/bin/python3


import json


#lambda functions for rounding
ro1, ro2, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 6), lambda x : round(x, 8)


# import coinGecko data
jsonInAddr = 'data/OGgecko.json'

with open(jsonInAddr, 'r') as f:
	geckoData = json.load(f)



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

for geckoKey in geckoKeys:
	currentGdict = geckoData[geckoKey]
	stdDev = stdDevFunc(currentGdict)
	currentGdict.update({'stdDev': stdDev})



# Need function to find percent change from 30Day low, high, and avg
# I.E. Need function to find 30Day low, high, and avg





# function to find percent change from 52Week low, high, and avg
def pChangeStatsFunc(analysisDict):
	#print(analysisDict)
	currentPair = analysisDict['pair']
	currentAvg = ro6(analysisDict['avg'])
	currentLowDate = list(analysisDict['min'].keys())[0]
	currentLow = ro6(analysisDict['min'][currentLowDate])
	currentHighDate = list(analysisDict['max'].keys())[0]
	currentHigh = ro6(analysisDict['max'][currentHighDate])
	currentData = analysisDict['data']
	#print("\n" + str(currentPair) + "52W Avg: $" + str(currentAvg))
	#print("52 Week High: " + str(currentHigh) + " on: " + str(currentHighDate))
	#print("52 Week Low: " + str(currentLow) + " on: " + str(currentLowDate) + "\n")
	currentDateList = list(currentData.keys())
	maxPchangeDict, minPchangeDict, avgPchangeDict = {}, {}, {}
	for date in currentDateList:
		datePrice = currentData[date]
		maxPchange = ro6(percentChange(currentHigh, datePrice))
		minPchange = ro6(percentChange(currentLow, datePrice))
		avgPchange = ro6(percentChange(currentAvg, datePrice))
		#print("Price: " + str(ro6(datePrice)) + " on: " + str(date))
		#print("pChange max: " + str(maxPchange) + "% pChange min: " + str(minPchange) + "% pChange Avg: " + str(avgPchange) + "%\n")
		maxPchangeDict.update({date: maxPchange})
		minPchangeDict.update({date: minPchange})
		avgPchangeDict.update({date: avgPchange})

		#pChangeDict = {'maxPchange': maxPchange, "minPchange": minPchange, 'avgPchange': avgPchange}
	analysisDict.update({'maxP': maxPchangeDict})
	analysisDict.update({'minP': minPchangeDict})
	analysisDict.update({'avgP': avgPchangeDict})


		#print(currentData)
	return analysisDict

quoteKeys = list(geckoData.keys())
for quoteKey in quoteKeys:
	currentTokenDict = geckoData[quoteKey]
	pChangeStatTest = pChangeStatsFunc(currentTokenDict)






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
