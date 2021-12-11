#!/usr/bin/python3

import numpy as np
from geckoFuncz import *

echoDtOutput = echoDt('Started', "Option Analysis")



#lambda functions for rounding
ro1, ro2, ro4, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4), lambda x : round(x, 6), lambda x : round(x, 8)


def putReturnFunc(currency, strikePrice, expPrice, numContracts, contractCost):

	if currency == 'btc':
		qtyBtc = numContracts * 0.01
		cost = ro2(numContracts * 0.01 * contractCost)
		fee = 0.15 * numContracts

		if strikePrice > expPrice:
			btcDifference = strikePrice - expPrice

			preFeeValue = btcDifference * qtyBtc
			value = ro2(preFeeValue - fee)

		else:
			value = ro2(-(cost + fee))

	elif currency == 'eth':

		qtyEth = numContracts * 0.1
		cost = ro2(numContracts * 0.1 * contractCost)
		fee = 0.15 * numContracts

		if strikePrice > expPrice:
			ethDifference = strikePrice - expPrice

			preFeeValue = ethDifference * qtyBtc
			value = ro2(preFeeValue - fee)

		else:
			value = ro2(-(cost + fee))



	putDictionary = {'strike': strikePrice, 'expiryPrice': expPrice, 'value': value, 'cost': cost, 'fee': fee, 'qty': numContracts}

	return putDictionary



def callReturnFunc(currency, strikePrice, expPrice, numContracts, contractCost):

	if currency == 'btc':
		qtyBtc = numContracts * 0.01
		cost = ro2(numContracts * 0.01 * contractCost)
		fee = 0.15 * numContracts

		if strikePrice < expPrice:
			btcDifference = expPrice - strikePrice

			preFeeValue = btcDifference * qtyBtc
			value = ro2(preFeeValue - fee)

		else:
			value = ro2(-(cost + fee))

	elif currency == 'eth':

		qtyEth = numContracts * 0.1
		cost = ro2(numContracts * 0.1 * contractCost)
		fee = 0.15 * numContracts

		if strikePrice < expPrice:
			ethDifference = expPrice - strikePrice

			preFeeValue = ethDifference * qtyBtc
			value = ro2(preFeeValue - fee)

		else:
			value = ro2(-(cost + fee))



	putDictionary = {'strike': strikePrice, 'expiryPrice': expPrice, 'value': value, 'cost': cost, 'fee': fee, 'qty': numContracts}

	return putDictionary






def strangleFunc(callOption, putOption):
	callValue, putValue = callOption['value'], putOption['value']
	callCost, putCost = callOption['cost'], putOption['cost']

	netValue = ro2(callValue + putValue)

	strangleDict = {'net': netValue, 'expiry': putOption['expiryPrice'], 'putStrike': putOption['strike'], 'callStrike': callOption['strike'], 'callCost': callCost, 'putCost': putCost}

	#print(callOption)
	#print(putOption)
	#print("\nNet Option Value: $" + str(netValue))
	return strangleDict


#print("Function output")
#testStrangle = strangleFunc(testCall, testPut)
#print(testStrangle)

def strangleResults(lowRange, highRange, rangeStep):
	strangleResultList = []
	for expiryPrice in np.arange(lowRange, highRange, rangeStep):
		testCall = callReturnFunc('btc', 50000, expiryPrice, 1, 1255)
		testPut = putReturnFunc('btc', 50000, expiryPrice, 1, 3607)
		strangle = strangleFunc(testCall, testPut)
		strangleResultList.append(strangle)
	return strangleResultList



strangleList = strangleResults(42000, 60000, 500)
#print(strangleList)


for strangleResult in strangleList:
	strangleCost = ro2(strangleResult['putCost'] + strangleResult['callCost'])
	#print(str(strangleResult['expiry']) + " " + str(strangleResult['net']))
	print(strangleResult)



"""
testContractPrice = 2593
testQty = 1
testStrikePrice = 48000

for btcPrice in np.arange(45000, 48100, 100):

	currentOptionDict = putReturnFunc('btc', testStrikePrice, btcPrice, testQty, testContractPrice)

	print(currentOptionDict)

"""



echoDtOutput = echoDt('Completed', "Option Analysis")

