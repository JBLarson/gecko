#!/usr/bin/python3

import numpy as np
from geckoFuncz import *

echoDtOutput = echoDt('Started', "Option Analysis")




def putReturnFunc(strikePrice, expPrice, numContracts, contractCost):

	qtyBtc = numContracts * 0.01
	cost = numContracts * 0.01 * contractCost
	fee = 0.15 * numContracts

	if strikePrice > expPrice:
		btcProfit = strikePrice - expPrice

		preFeeValue = btcProfit * qtyBtc
		value = preFeeValue - fee

	else:
		value = -(cost + fee)



	putDictionary = {'strikePrice': strikePrice, 'expiryPrice': expPrice, 'value': value, 'cost': cost, 'fee': fee, 'qty': numContracts}

	return putDictionary




#test1 = putReturnFunc(50000, 4625, 4, 695)

#print("\nFunction output")
#print(test1)

testContractPrice = 2593
testQty = 4
testStrikePrice = 52000

for btcPrice in np.arange(45000, 55000, 500):

	currentOptionDict = putReturnFunc(testStrikePrice, btcPrice, testQty, testContractPrice)

	print(currentOptionDict)





echoDtOutput = echoDt('Completed', "Option Analysis")

