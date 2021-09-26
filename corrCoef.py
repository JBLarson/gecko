#!/usr/bin/python3

from geckoFuncz import readJsonFunc, createJsonFunc, echoDt
import numpy as np


echoDtOutput = echoDt('Started', "Correlation Coefficient")




#lambda functions for rounding
ro1, ro2, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 6), lambda x : round(x, 8)




geckoData = readJsonFunc('data/geckoAnalysis2.json')
geckoKeys = list(geckoData.keys())


def correlationCoefficient(list1, list2):
	corrCoef = np.corrcoef(list1, list2)
	return corrCoef



def btcCorrCoefFunc(tokenPair):
	tokenPrices = list(geckoData[tokenPair]['data'].values())
	if 'Usd' in tokenPair:	btcPrices = list(geckoData['BtcUsd']['data'].values())
	if 'Eur' in tokenPair:	btcPrices = list(geckoData['BtcEur']['data'].values())
	corrCoefOutput = float(correlationCoefficient(btcPrices, tokenPrices)[0,1])

	return corrCoefOutput


#for geckoKey in geckoKeys:
#	btcCorrCoef = btcCorrCoefFunc(geckoKey)
#	print(geckoKey + " BTC Corr Coef: " + str(btcCorrCoef))







def corrCoefNFunc(tokenPair):
	tokenPrices = list(geckoData[tokenPair]['data'].values())
	if 'Usd' in tokenPair:	btcPrices = list(geckoData['BtcUsd']['data'].values())
	elif 'Eur' in tokenPair:	btcPrices = list(geckoData['BtcEur']['data'].values())
	corrCoefBtc = float(correlationCoefficient(btcPrices, tokenPrices)[0,1])

	if 'Usd' in tokenPair:	ethPrices = list(geckoData['EthUsd']['data'].values())
	elif 'Eur' in tokenPair:	ethPrices = list(geckoData['EthEur']['data'].values())
	corrCoefEth = float(correlationCoefficient(ethPrices, tokenPrices)[0,1])

	corrCoefOutput = {'btc': corrCoefBtc, 'eth': corrCoefEth}

	return corrCoefOutput





for geckoKey in geckoKeys:
	corrCoef = corrCoefNFunc(geckoKey)
	print("Currency Pair: " + geckoKey + " Corr Coefs: " + str(corrCoef))




echoDtOutput = echoDt('Completed', "Correlation Coefficient")
