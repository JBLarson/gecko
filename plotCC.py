

from geckoFuncz import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# lambda funcs

ro1, ro2, ro4, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4), lambda x : round(x, 6), lambda x : round(x, 8)


ccDict = readJsonFunc('data/cc.json')
geckoData = readJsonFunc('data/gData2.json')


ethUsd, kavaUsd = geckoData['EthUsd'], geckoData['KavaUsd']


print(ethUsd.keys())
print('\n')



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



"""


def analyzeCrypto(inputCrypto):
	quoteCurrency = inputCrypto['quote']

	price, volume = inputCrypto['data'], inputCrypto['volumeData']
	avg0, max0, min0, stdDev0 = inputCrypto['avg'], inputCrypto['max'], inputCrypto['min'], inputCrypto['stdDev']


	print(avg0)
	dateList = list(price.keys())
	dList, pList, vList = [], [], []
	for iDate in dateList[0:30]:
		
		print('\n')
		dList.append(iDate)
		pList.append(price[iDate])
		vList.append(volume[iDate])

		print(volume[iDate])

	

	figure, axis = plt.subplots(2, 2)

	
	axis[0, 0].plot(dList, pList)
	axis[0, 0].set_title("Price")

	axis[0, 1].plot(dList, vList)
	axis[0, 1].set_title("Volume")

	axis[1, 0].plot(dList, pList)
	axis[1, 0].set_title("Price")

	axis[1, 1].plot(dList, vList)
	axis[1, 1].set_title("Price")



	plt.show()

analyzeCrypto(ethUsd)
	"""






def plotTwo(inputCrypto0, inputCrypto1):
	quoteCurrency0, quoteCurrency1 = inputCrypto0['quote'], inputCrypto1['quote']

	price0, volume0 = inputCrypto0['data'], inputCrypto0['volumeData']
	avg0, max0, min0, stdDev0 = inputCrypto0['avg'], inputCrypto0['max'], inputCrypto0['min'], inputCrypto0['stdDev']


	price1, volume1 = inputCrypto1['data'], inputCrypto1['volumeData']
	avg1, max1, min1, stdDev1 = inputCrypto1['avg'], inputCrypto1['max'], inputCrypto1['min'], inputCrypto1['stdDev']



	print(quoteCurrency0)
	print('&')
	print(quoteCurrency1)


	dateList = list(price0.keys())
	dList, pList0, vList0 = [], [], []
	pList1, vList1 = [], []
	
	for iDate in dateList[0:30]:
		
		print('\n')
		dList.append(iDate)
		pList0.append(price0[iDate])
		vList0.append(volume0[iDate])
		pList1.append(price1[iDate])
		vList1.append(volume1[iDate])

		print(volume1[iDate])

	

	figure, axis = plt.subplots(2, 2)

	
	axis[0, 0].plot(dList, pList0)
	axis[0, 0].set_title("Price")

	axis[0, 1].plot(dList, vList0)
	axis[0, 1].set_title("Volume")

	axis[1, 0].plot(dList, pList1)
	axis[1, 0].set_title("Price")

	axis[1, 1].plot(dList, vList1)
	axis[1, 1].set_title("Price")



	plt.show()


gTest = plotTwo(ethUsd, kavaUsd)




# make it with just one plot



