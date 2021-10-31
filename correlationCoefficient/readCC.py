#!/usr/bin/python3

from geckoFuncz import *



echoDtOutput = echoDt('Started', "Correlation Coefficient Analysis")



ccData = readJsonFunc('data/cc.json')





ccTimeFrames = list(ccData.keys())



geckoKeys = list(ccData[ccTimeFrames[0]].keys())


def ccStats(currentCCdata):
	currentCCList = []
	firstCC = currentCCdata[geckoKeys[0]]

	minCorr, maxCorr, corrSum = {geckoKeys[0]: firstCC}, {geckoKeys[0]: firstCC}, 0

	for currentCompKey in geckoKeys:
		currentCC = currentCCdata[currentCompKey]

		currentCCList.append(currentCC)
		#print(str(currentCompKey) + "  " + str(currentCC))
		corrSum += currentCC
	#print(currentCCList)

	avgCorr = corrSum / len(geckoKeys)

	ccStatOutput = {'max': maxCorr, 'min': minCorr, 'avg': avgCorr}

	return ccStatOutput


for ccTimeFrame in ccTimeFrames:
	print("\n\n" + str(ccTimeFrame) + "-day moving avg\n")
	currentCCtimeframe = ccData[ccTimeFrame]
	for geckoKey in geckoKeys:
		currentCCdata = currentCCtimeframe[geckoKey]
		#print(currentCCdata)
		currentCCStats = ccStats(currentCCdata)

		print("\nCC stats for: " + str(geckoKey) + " " + str(currentCCStats))



echoDtOutput = echoDt('Completed', "Correlation Coefficient Analysis")
