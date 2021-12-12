#!/usr/bin/python3

import numpy as np
from geckoFuncz import *
import matplotlib.pyplot as plt


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

		else:	value = ro2(-(cost + fee))

	elif currency == 'eth':
		qtyEth = numContracts * 0.1
		cost = ro2(numContracts * 0.1 * contractCost)
		fee = 0.15 * numContracts
		if strikePrice > expPrice:
			ethDifference = strikePrice - expPrice
			preFeeValue = ethDifference * qtyEth
			value = ro2(preFeeValue - fee)

		else:	value = ro2(-(cost + fee))

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

		else:	value = ro2(-(cost + fee))

	elif currency == 'eth':

		qtyEth = numContracts * 0.1
		cost = ro2(numContracts * 0.1 * contractCost)
		fee = 0.15 * numContracts
		if strikePrice < expPrice:
			ethDifference = expPrice - strikePrice
			preFeeValue = ethDifference * qtyEth
			value = ro2(preFeeValue - fee)

		else:	value = ro2(-(cost + fee))



	putDictionary = {'strike': strikePrice, 'expiryPrice': expPrice, 'value': value, 'cost': cost, 'fee': fee, 'qty': numContracts}

	return putDictionary






def strangleFunc(callOption, putOption):
	callValue, putValue = callOption['value'], putOption['value']
	callCost, putCost = callOption['cost'], putOption['cost']

	netValue = ro2(callValue + putValue)

	strangleDict = {'net': netValue, 'expiry': putOption['expiryPrice'], 'putStrike': putOption['strike'], 'callStrike': callOption['strike'], 'callCost': callCost, 'putCost': putCost}

	return strangleDict



def strangleEth(lowRange, highRange, rangeStep):
	strangleResultList = []
	for expiryPrice in np.arange(lowRange, highRange, rangeStep):
		testCall = callReturnFunc('eth', 4000, expiryPrice, 1, 390)
		testPut = putReturnFunc('eth', 4000, expiryPrice, 1, 400)
		strangle = strangleFunc(testCall, testPut)
		strangleResultList.append(strangle)
	return strangleResultList




def strangleBtcOg(lowRange, highRange, rangeStep):
	strangleResultList = []
	for expiryPrice in np.arange(lowRange, highRange, rangeStep):
		testCall = callReturnFunc('btc', 50000, expiryPrice, 1, 1200)
		testPut = putReturnFunc('btc', 50000, expiryPrice, 2, 2900)
		strangle = strangleFunc(testCall, testPut)
		strangleResultList.append(strangle)
	return strangleResultList



def strangleBtc(lowRange, highRange, rangeStep, strike, callCost, callQty, putCost, putQty):
	strangleResultList = []
	for expiryPrice in np.arange(lowRange, highRange, rangeStep):
		testCall = callReturnFunc('btc', strike, expiryPrice, callQty, callCost)
		testPut = putReturnFunc('btc', strike, expiryPrice, putQty, putCost)
		strangle = strangleFunc(testCall, testPut)
		strangleResultList.append(strangle)
	return strangleResultList



def getPlotLists(strangleList):
	expiryList, netList, strikeList = [], [], []

	for strangleResult in strangleList:
		#print(strangleResult)
		strangleCost = ro2(strangleResult['putCost'] + strangleResult['callCost'])
		currentExpiry = strangleResult['expiry']
		currentNet = strangleResult['net']
		currentStrike = strangleResult['putStrike']
		expiryList.append(currentExpiry)
		netList.append(currentNet)
		strikeList.append(currentStrike)

	plotDict = {'expiry': expiryList, 'net': netList, 'strike': strikeList}

	return plotDict



#strangleEth = strangleEth(3000, 5000, 200)
strangleBtc0 = strangleBtc(39999, 60001, 250, 50000, 1200, 1, 2900, 2)
strangleBtc1 = strangleBtc(39999, 60001, 250, 50000, 1110, 1, 2819, 1)



plotBtc0 = getPlotLists(strangleBtc0)
plotBtc1 = getPlotLists(strangleBtc1)

expiryList0, netList0 = plotBtc0['expiry'], plotBtc0['net']

expiryList1, netList1 = plotBtc1['expiry'], plotBtc1['net']

fig = plt.figure(figsize=(8, 4))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

ax1.plot(expiryList0, netList0)
ax2.plot(expiryList1, netList1)

plt.show()



echoDtOutput = echoDt('Completed', "Option Analysis")
