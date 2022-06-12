#!/usr/bin/python3

from time import *
from datetime import *
import json
from geckoFuncz import *
import math
import dateparser



#lambda functions for rounding
ro1, ro2, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 6), lambda x : round(x, 8)

# ---
# gecko API request section
# ---


time = datetime.datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nStarted fetching coin data on: " + str(justDate) + " at: " + str(justTime))


# import symbolName data
symbolNamesInAddr = 'data/symbolNames.json'

with open(symbolNamesInAddr, 'r') as r:
	symbolNameDict = json.load(r)


geckoData = getAllTokens(symbolNameDict)


time = datetime.datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nCompleted fetching coin data on: " + str(justDate) + " at: " + str(justTime))


# ---
# sample stats section
# ---


time = datetime.datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nStarted creating sample stats on: " + str(justDate) + " at: " + str(justTime))


geckoKeys = list(geckoData.keys())


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
	stdDev = stdDevFunc(currentGdict)
	currentGdict.update({'stdDev': stdDev})




time = datetime.datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nCompleted creating sample stats on: " + str(justDate) + " at: " + str(justTime))




jsonOutAddr = 'data/geckoAnalysis.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(geckoData, fp1)

	print("\nSuccess saving JSON file at: " + str(jsonOutAddr) + '\n')


except Exception as e: print(e)




