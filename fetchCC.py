#!/usr/bin/python3

from geckoFuncz import readJsonFunc, createJsonFunc
import numpy as np








def percentChange(fromNum, toNum):
	pChange = ((toNum - fromNum)/fromNum)*100
	return pChange




def pChangeFuncVol(tokenDict):
	pChangeDict = {}
	tokenVolumes = tokenDict['volumeData']
	tokenDates = list(tokenVolumes.keys())
	for currentDate in tokenDates:
		dateIndex = tokenDates.index(currentDate)
		currentVol = tokenVolumes[currentDate]
		if dateIndex != 0:
			lastDate = tokenDates[dateIndex-1]
			lastVol = tokenVolumes[lastDate]
			currentPChange = percentChange(lastVol, currentVol)
			pChangeDict.update({currentDate: currentPChange})

	return pChangeDict


def pChangeFunc(tokenDict):
	pChangeDict = {}
	tokenPrices = tokenDict['data']
	tokenDates = list(tokenPrices.keys())
	for currentDate in tokenDates:
		dateIndex = tokenDates.index(currentDate)
		currentPrice = tokenPrices[currentDate]
		if dateIndex != 0:
			lastDate = tokenDates[dateIndex-1]
			lastPrice = tokenPrices[lastDate]
			currentPChange = percentChange(lastPrice, currentPrice)
			pChangeDict.update({currentDate: currentPChange})


	return pChangeDict








#lambda functions for rounding
ro1, ro2, ro4, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4), lambda x : round(x, 6), lambda x : round(x, 8)


geckoData = readJsonFunc('data/gData.json')
geckoKeys = list(geckoData.keys())

"""
ethUsd = geckoData['EthUsd']

print(ethUsd)

print('\n')

print(geckoKeys)
print('\nGecko keys above eth below')
print(ethUsd.keys())


ethPrices = ethUsd['data']

print(ethPrices)
priceDates = list(ethPrices.keys())



for pDate in priceDates:

	price = ethPrices[pDate]
	print(price)


"""






# find daily percentage change for each token price
for geckoKey in geckoKeys:
	currentTokenDict = geckoData[geckoKey]
	pChangeDict = pChangeFunc(currentTokenDict)
	currentTokenDict['pChange'] = pChangeDict




# find daily percentage change for each token vol
for geckoKey in geckoKeys:
	currentTokenDict = geckoData[geckoKey]
	pChangeDict = pChangeFuncVol(currentTokenDict)
	currentTokenDict['vpChange'] = pChangeDict




#print(geckoData)



createJsonFunc('data/gData2.json', geckoData)

geckoData = readJsonFunc('data/gData2.json')




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
		KavaPrices = list(geckoData['KavaUsd']['pChange'].values())
		XmrPrices = list(geckoData['XmrUsd']['pChange'].values())
		daiPrices = list(geckoData['DaiUsd']['pChange'].values())


	elif 'Eur' in geckoKey:
		btcPrices = list(geckoData['BtcEur']['pChange'].values())
		ethPrices = list(geckoData['EthEur']['pChange'].values())
		KavaPrices = list(geckoData['KavaEur']['pChange'].values())
		XmrPrices = list(geckoData['XmrEur']['pChange'].values())
		daiPrices = list(geckoData['DaiEur']['pChange'].values())


	corrCoefBtc = ro4(float(correlationCoefficient(btcPrices, tokenPrices)[0,1]))
	corrCoefEth = ro4(float(correlationCoefficient(ethPrices, tokenPrices)[0,1]))
	corrCoefKava = ro4(float(correlationCoefficient(KavaPrices, tokenPrices)[0,1]))
	corrCoefXmr = ro4(float(correlationCoefficient(XmrPrices, tokenPrices)[0,1]))
	corrCoefDai = ro4(float(correlationCoefficient(daiPrices, tokenPrices)[0,1]))


	corrCoefOutput = {'btc': corrCoefBtc, 'eth': corrCoefEth, 'Kava': corrCoefKava, 'Xmr': corrCoefXmr, 'dai': corrCoefDai}


	return corrCoefOutput




def movingCorrCoefFunc(geckoKey, n):

	tokenPrices = list(geckoData[geckoKey]['pChange'].values())[-n-1: -1]


	if 'Usd' in geckoKey:
		btcPrices = list(geckoData['BtcUsd']['pChange'].values())[-n-1: -1]
		ethPrices = list(geckoData['EthUsd']['pChange'].values())[-n-1: -1]
		KavaPrices = list(geckoData['KavaUsd']['pChange'].values())[-n-1: -1]
		XmrPrices = list(geckoData['XmrUsd']['pChange'].values())[-n-1: -1]
		daiPrices = list(geckoData['DaiUsd']['pChange'].values())[-n-1: -1]


	corrCoefBtc = ro4(float(correlationCoefficient(btcPrices, tokenPrices)[0,1]))
	corrCoefEth = ro4(float(correlationCoefficient(ethPrices, tokenPrices)[0,1]))
	corrCoefKava = ro4(float(correlationCoefficient(KavaPrices, tokenPrices)[0,1]))
	corrCoefXmr = ro4(float(correlationCoefficient(XmrPrices, tokenPrices)[0,1]))
	corrCoefDai = ro4(float(correlationCoefficient(daiPrices, tokenPrices)[0,1]))


	corrCoefOutput = {'btc': corrCoefBtc, 'eth': corrCoefEth, 'Kava': corrCoefKava, 'Xmr': corrCoefXmr, 'dai': corrCoefDai}


	return corrCoefOutput





cc365Dict, cc180Dict, cc90Dict, cc30Dict = {}, {}, {}, {}

for geckoKey in geckoKeys:
	corrCoef = allCorrCoefFunc(geckoKey)
	cc365Dict.update({geckoKey: corrCoef})


for geckoKey in geckoKeys:
	corrCoef = movingCorrCoefFunc(geckoKey, 180)
	cc180Dict.update({geckoKey: corrCoef})


for geckoKey in geckoKeys:
	corrCoef = movingCorrCoefFunc(geckoKey, 90)
	cc90Dict.update({geckoKey: corrCoef})



for geckoKey in geckoKeys:
	corrCoef = movingCorrCoefFunc(geckoKey, 30)
	cc30Dict.update({geckoKey: corrCoef})
	
	print("Currency Pair: " + geckoKey + " Corr Coefs: " + str(corrCoef))



#print("\n7-day Corr Coef")
#for geckoKey in geckoKeys:	corrCoef = movingCorrCoefFunc(geckoKey, 7)
	
#print("Currency Pair: " + geckoKey + " Corr Coefs: " + str(corrCoef))


ccData = {'30': cc30Dict, '90':cc90Dict, '180': cc180Dict, '365': cc365Dict}

try:
	createJsonFunc('data/cc.json', ccData)
	print('\nsuccess saving CC data')
except Exception as e:
	print('\nFailed to save. Exception:')
	print(e)




print('\nComplete\n')

