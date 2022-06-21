

from geckoFuncz import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# lambda funcs

ro1, ro2, ro4, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4), lambda x : round(x, 6), lambda x : round(x, 8)


ccDict = readJsonFunc('data/cc.json')
geckoData = readJsonFunc('data/gData2.json')


ethUsd = geckoData['EthUsd']


print(ethUsd.keys())
#print('\n')

def analyzeGeckoOld(inputGecko):
	geckoKeys = list(inputGecko.keys())
	for key in geckoKeys:
		print('\n')
		print(key)
		currentCrypto = geckoData[key]
		currentKeys = list(currentCrypto.keys())

		for key in currentKeys[0:]:
			print(key)
			#print(currentCrypto[key])






def analyzeCrypto(inputCrypto):
	quoteCurrency = inputCrypto['quote']

	price, volume = inputCrypto['data'], inputCrypto['volumeData']
	avg0, max0, min0, stdDev0 = inputCrypto['avg'], inputCrypto['max'], inputCrypto['min'], inputCrypto['stdDev']


	print(avg0)
	dateList = list(price.keys())
	pList, vList = [], []
	for iDate in dateList:
		
		print('\n')
		print(iDate)
		pList.append(price[iDate])
		vList.append(volume[iDate])

		print(volume[iDate])

	

	figure, axis = plt.subplots(2, 2)

	
	axis[0, 0].plot(dateList, pList)
	axis[0, 0].set_title("Price")

	axis[0, 1].plot(dateList, vList)
	axis[0, 1].set_title("Price")

	plt.show()


gTest = analyzeCrypto(ethUsd)





