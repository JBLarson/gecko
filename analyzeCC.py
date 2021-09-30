#!/usr/bin/python3

from geckoFuncz import *


ccData = readJsonFunc('data/cc.json')


ccTimeFrames = list(ccData.keys())



geckoKeys = list(ccData[ccTimeFrames[0]].keys())


for ccTimeFrame in ccTimeFrames[-1:]:
	print("\n\n" + str(ccTimeFrame) + "-day moving avg\n")
	currentCCtimeframe = ccData[ccTimeFrame]
	for geckoKey in geckoKeys:
		print("\nCorrelation Coefficient data for: " + str(geckoKey))
		currentCCdata = currentCCtimeframe[geckoKey]
		#print(currentCCdata)
		for currentCompKey in geckoKeys:

			currentCC = currentCCdata[currentCompKey]
			print(str(currentCompKey) + "  " + str(currentCC))

