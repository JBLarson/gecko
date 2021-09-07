#!/usr/bin/python3

import time
import datetime
import dateparser
import json
import math
import matplotlib.pyplot as plt

#lambda functions for rounding
ro1, ro2, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 6), lambda x : round(x, 8)


# import coinGecko data
jsonInAddr = 'data/geckoAnalysis2.json'
with open(jsonInAddr, 'r') as f:
	geckoData = json.load(f)


def describeData(geckoData):
	geckoKeys = list(geckoData.keys())
	for geckoKey in geckoKeys:
		print("\n" + geckoData[geckoKey]['pair'])
		print("Avg: " + str(geckoData[geckoKey]['avg']))
		print("StdDev: " + str(geckoData[geckoKey]['stdDev']))
		print("Min: " + str(geckoData[geckoKey]['min']))
		print("Max: " + str(geckoData[geckoKey]['max']))

"""
adaUsd = geckoData['AdaUsd']
adaUsdMovingAvg = adaUsd['movingAvg30']
adaUsdPrices = adaUsd['data']
adaUsdStdDev = adaUsd['stdDev']
adaUsdVolume = adaUsd['volumeData']

movingAvgKeys = list(adaUsdMovingAvg.keys())


smaDates, smaPrices, prices, volumes = [], [], [], []

for key in movingAvgKeys:
	smaDates.append(key)
	smaPrices.append(adaUsdMovingAvg[key])
	prices.append(adaUsdPrices[key])
	volumes.append(adaUsdVolume[key])


plt.subplot(211)
plt.plot(smaDates, smaPrices)

plt.ylabel('Price')

plt.plot(smaDates, prices)
plt.title('AdaUsd Prices and SMA')

plt.subplot(212)
plt.plot(smaDates, volumes)
plt.title('AdaUsd Volume')
plt.ylabel('Volume')


plt.show()
"""

def plotTokenFunc(tokenSymbol):
	tokenPair = geckoData[tokenSymbol]
	tokenPairMovingAvg30 = tokenPair['movingAvg30']
	tokenPairMovingAvg50 = tokenPair['movingAvg50']
	tokenPairMovingAvg200 = tokenPair['movingAvg200']

	tokenPairPrices = tokenPair['data']
	tokenPairStdDev = tokenPair['stdDev']
	tokenPairVolume = tokenPair['volumeData']

	movingAvgKeys = list(tokenPairMovingAvg30.keys())


	smaDates, sma30Prices, sma50Prices, sma200Prices, prices, volumes = [], [], [], [], [], []

	for key in movingAvgKeys:
		smaDates.append(key)
		sma30Prices.append(tokenPairMovingAvg30[key])
		sma50Prices.append(tokenPairMovingAvg50[key])
		sma200Prices.append(tokenPairMovingAvg200[key])

		prices.append(tokenPairPrices[key])
		volumes.append(tokenPairVolume[key])


	plt.subplot(211)
	#plt.plot(smaDates, sma30Prices)
	plt.plot(smaDates, sma50Prices)
	plt.plot(smaDates, sma200Prices)

	plt.ylabel('Price')

	plt.plot(smaDates, prices)
	priceTitle = tokenSymbol + " Prices and SMA"
	plt.title(priceTitle)
	plt.subplot(212)
	plt.plot(smaDates, volumes)
	volumeTitle = tokenSymbol + " Volume"
	plt.title(volumeTitle)


	plt.show()

#plotAda = plotTokenFunc('AdaUsd')
#plotBtc = plotTokenFunc('BtcUsd')
plotEth = plotTokenFunc('EthUsd')
