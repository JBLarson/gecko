#!/usr/bin/python3

from geckoFuncz import *


ccData = readJsonFunc('data/cc.json')


ccTimeFrames = list(ccData.keys())



geckoKeys = list(ccData[ccTimeFrames[0]].keys())


for ccTimeFrame in ccTimeFrames:
	currentCCtimeframe = ccData[ccTimeFrame]
	for geckoKey in geckoKeys:
		print("\nCorrelation Coefficient data for: " + str(geckoKey))
		currentCCdata = currentCCtimeframe[geckoKey]
		print(currentCCdata)

