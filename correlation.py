#!/usr/bin/python3

from geckoFuncz import readJsonFunc, createJsonFunc, echoDt
import numpy as np


echoDtOutput = echoDt('Started', "Correlation Coefficient")




#lambda functions for rounding
ro1, ro2, ro4, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4), lambda x : round(x, 6), lambda x : round(x, 8)




geckoData = readJsonFunc('data/geckoAnalysis.json')
geckoKeys = list(geckoData.keys())




def correlationCoefficient(list1, list2):
	corrCoef = np.corrcoef(list1, list2)
	return corrCoef



def corrCoefFunc(tokenPair):
	tokenPrices = list(geckoData[tokenPair]['data'].values())
	if 'Usd' in tokenPair:	btcPrices = list(geckoData['BtcUsd']['data'].values())
	elif 'Eur' in tokenPair:	btcPrices = list(geckoData['BtcEur']['data'].values())
	corrCoefBtc = ro6(float(correlationCoefficient(btcPrices, tokenPrices)[0,1]))

	if 'Usd' in tokenPair:	ethPrices = list(geckoData['EthUsd']['data'].values())
	elif 'Eur' in tokenPair:	ethPrices = list(geckoData['EthEur']['data'].values())
	corrCoefEth = ro6(float(correlationCoefficient(ethPrices, tokenPrices)[0,1]))

	corrCoefOutput = {'btc': corrCoefBtc, 'eth': corrCoefEth}

	return corrCoefOutput






def allCorrCoefFunc(geckoKey):

	tokenPrices = list(geckoData[geckoKey]['pChange'].values())

	if 'Usd' in geckoKey:
		btcPrices = list(geckoData['BtcUsd']['pChange'].values())
		ethPrices = list(geckoData['EthUsd']['pChange'].values())
		adaPrices = list(geckoData['AdaUsd']['pChange'].values())
		linkPrices = list(geckoData['LinkUsd']['pChange'].values())
		daiPrices = list(geckoData['DaiUsd']['pChange'].values())


	elif 'Eur' in geckoKey:
		btcPrices = list(geckoData['BtcEur']['pChange'].values())
		ethPrices = list(geckoData['EthEur']['pChange'].values())
		adaPrices = list(geckoData['AdaEur']['pChange'].values())
		linkPrices = list(geckoData['LinkEur']['pChange'].values())
		daiPrices = list(geckoData['DaiEur']['pChange'].values())


	corrCoefBtc = ro4(float(correlationCoefficient(btcPrices, tokenPrices)[0,1]))
	corrCoefEth = ro4(float(correlationCoefficient(ethPrices, tokenPrices)[0,1]))
	corrCoefAda = ro4(float(correlationCoefficient(adaPrices, tokenPrices)[0,1]))
	corrCoefLink = ro4(float(correlationCoefficient(linkPrices, tokenPrices)[0,1]))
	corrCoefDai = ro4(float(correlationCoefficient(daiPrices, tokenPrices)[0,1]))


	corrCoefOutput = {'btc': corrCoefBtc, 'eth': corrCoefEth, 'ada': corrCoefAda, 'link': corrCoefLink, 'dai': corrCoefDai}


	return corrCoefOutput




def movingCorrCoefFunc(geckoKey, n):

	tokenPrices = list(geckoData[geckoKey]['pChange'].values())[-n-1: -1]


	if 'Usd' in geckoKey:
		btcPrices = list(geckoData['BtcUsd']['pChange'].values())[-n-1: -1]
		ethPrices = list(geckoData['EthUsd']['pChange'].values())[-n-1: -1]
		adaPrices = list(geckoData['AdaUsd']['pChange'].values())[-n-1: -1]
		linkPrices = list(geckoData['LinkUsd']['pChange'].values())[-n-1: -1]
		daiPrices = list(geckoData['DaiUsd']['pChange'].values())[-n-1: -1]


	elif 'Eur' in geckoKey:
		btcPrices = list(geckoData['BtcEur']['pChange'].values())[-n-1: -1]
		ethPrices = list(geckoData['EthEur']['pChange'].values())[-n-1: -1]
		adaPrices = list(geckoData['AdaEur']['pChange'].values())[-n-1: -1]
		linkPrices = list(geckoData['LinkEur']['pChange'].values())[-n-1: -1]
		daiPrices = list(geckoData['DaiEur']['pChange'].values())[-n-1: -1]


	corrCoefBtc = ro4(float(correlationCoefficient(btcPrices, tokenPrices)[0,1]))
	corrCoefEth = ro4(float(correlationCoefficient(ethPrices, tokenPrices)[0,1]))
	corrCoefAda = ro4(float(correlationCoefficient(adaPrices, tokenPrices)[0,1]))
	corrCoefLink = ro4(float(correlationCoefficient(linkPrices, tokenPrices)[0,1]))
	corrCoefDai = ro4(float(correlationCoefficient(daiPrices, tokenPrices)[0,1]))


	corrCoefOutput = {'btc': corrCoefBtc, 'eth': corrCoefEth, 'ada': corrCoefAda, 'link': corrCoefLink, 'dai': corrCoefDai}


	return corrCoefOutput



print("\n52-week Corr Coef")


for geckoKey in geckoKeys:
	corrCoef = allCorrCoefFunc(geckoKey)
	print("Currency Pair: " + geckoKey + " Corr Coefs: " + str(corrCoef))



print("\n30-day Corr Coef")


for geckoKey in geckoKeys:
	corrCoef = movingCorrCoefFunc(geckoKey, 30)
	print("Currency Pair: " + geckoKey + " Corr Coefs: " + str(corrCoef))



print("\n7-day Corr Coef")
for geckoKey in geckoKeys:
	corrCoef = movingCorrCoefFunc(geckoKey, 7)
	print("Currency Pair: " + geckoKey + " Corr Coefs: " + str(corrCoef))






echoDtOutput = echoDt('Completed', "Correlation Coefficient")
