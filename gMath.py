


# function that returns high price in price dict
def maxFunc(targetDict):
	firstKey = (list(targetDict.keys()))[0]
	maxItem = {firstKey: targetDict[firstKey]}
	targetKeys = targetDict.keys()
	for targetKey in targetKeys:
		maxDate = list(maxItem.keys())[0]
		if targetDict[targetKey] > maxItem[maxDate]:
			maxItem = {targetKey: targetDict[targetKey]}
	return maxItem




# function that returns low price in price dict
def minFunc(targetDict):
	firstKey = (list(targetDict.keys()))[0]
	minItem = {firstKey: targetDict[firstKey]}
	targetKeys = targetDict.keys()
	for targetKey in targetKeys:
		minDate = list(minItem.keys())[0]
		if targetDict[targetKey] < minItem[minDate]:
			minItem = {targetKey: targetDict[targetKey]}
	return minItem





# function that returns avg price for priceDict
def avgFunc(targetDict):
	targetList = list(targetDict.values())
	sumOfRates = 0
	for rate in targetList:
		sumOfRates += int(rate)

	avgRate = sumOfRates / len(targetList)
	return avgRate

