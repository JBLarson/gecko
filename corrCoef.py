#!/usr/bin/python3

from geckoFuncz import readJsonFunc, createJsonFunc, echoDt
import numpy as np


echoDtOutput = echoDt('Started', "Correlation Coefficient")


geckoData = readJsonFunc('data/geckoAnalysis2.json')
geckoKeys = list(geckoData.keys())


def correlationCoefficient(list1, list2):
	corrCoef = np.corrcoef(list1, list2)
	return corrCoef


def corrCoefFunc(tokenPair):
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
	corrCoef = corrCoefFunc(geckoKey)
	print(geckoKey + " Corr Coefs: " + str(corrCoef))




echoDtOutput = echoDt('Completed', "Correlation Coefficient")
