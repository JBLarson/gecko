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

	tokenPrices = list(geckoData[geckoKey]['data'].values())

	if 'Usd' in geckoKey:
		btcPrices = list(geckoData['BtcUsd']['data'].values())
		ethPrices = list(geckoData['EthUsd']['data'].values())
		adaPrices = list(geckoData['AdaUsd']['data'].values())
		linkPrices = list(geckoData['LinkUsd']['data'].values())
		daiPrices = list(geckoData['DaiUsd']['data'].values())


	elif 'Eur' in geckoKey:
		btcPrices = list(geckoData['BtcEur']['data'].values())
		ethPrices = list(geckoData['EthEur']['data'].values())
		adaPrices = list(geckoData['AdaEur']['data'].values())
		linkPrices = list(geckoData['LinkEur']['data'].values())
		daiPrices = list(geckoData['DaiEur']['data'].values())


	

	corrCoefBtc = ro6(float(correlationCoefficient(btcPrices, tokenPrices)[0,1]))
	corrCoefEth = ro6(float(correlationCoefficient(ethPrices, tokenPrices)[0,1]))
	corrCoefAda = ro6(float(correlationCoefficient(adaPrices, tokenPrices)[0,1]))
	corrCoefLink = ro6(float(correlationCoefficient(linkPrices, tokenPrices)[0,1]))
	corrCoefDai = ro6(float(correlationCoefficient(daiPrices, tokenPrices)[0,1]))


	corrCoefOutput = {'btc': corrCoefBtc, 'eth': corrCoefEth, 'ada': corrCoefAda, 'link': corrCoefLink, 'dai': corrCoefDai}

	#except Exception as e:
	#	print("\nException: " + str(e) + "\n")

	return corrCoefOutput





for geckoKey in geckoKeys:
	corrCoef = allCorrCoefFunc(geckoKey)
	print("Currency Pair: " + geckoKey + " Corr Coefs: " + str(corrCoef))





echoDtOutput = echoDt('Completed', "Correlation Coefficient")
