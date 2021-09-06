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
jsonInAddr = 'data/geckoAnalysis.json'
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


adaUsd = geckoData['AdaUsd']
adaUsdMovingAvg = adaUsd['movingAvg30']
adaUsdPrices = adaUsd['data']
adaUsdStdDev = adaUsd['stdDev']

movingAvgKeys = list(adaUsdMovingAvg.keys())


smaDates, smaPrices, prices = [], [], []

for key in movingAvgKeys:
	smaDates.append(key)
	smaPrices.append(adaUsdMovingAvg[key])
	prices.append(adaUsdPrices[key])



#plt.subplot(121)
plt.plot(smaDates, smaPrices)
#plt.title('AdaUsd Simple Moving Average')


#plt.subplot(122)
plt.plot(smaDates, prices)
plt.title('AdaUsd Prices and SMA')


#plt.ylabel('Price')
#plt.xlabel('Dates')

plt.show()

