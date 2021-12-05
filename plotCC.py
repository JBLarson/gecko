#!/usr/bin/python3

from geckoFuncz import readJsonFunc, createJsonFunc, echoDt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


echoDtOutput = echoDt('Started', "Correlation Coefficient")




#lambda functions for rounding
ro1, ro2, ro4, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4), lambda x : round(x, 6), lambda x : round(x, 8)




geckoData = readJsonFunc('data/geckoAnalysis.json')
geckoKeys = list(geckoData.keys())

btcData = geckoData['BtcUsd']


def correlationCoefficient(list1, list2):
	corrCoef = np.corrcoef(list1, list2)
	return corrCoef


def weekPriceFunc(tokenPair):
	btcData = geckoData[tokenPair]

	btcPchange = (btcData['pChange'])

	priceDates = list(btcPchange.keys())
	prices = list(btcPchange.values())

	i = 0
	weekPriceDicts = {}
	while i < len(priceDates):
		if i > 3:
		
		
			#print(currentDate)
			try:

				currentDate = priceDates[i]
				lastDay = priceDates[i-1]
				nextDay = priceDates[i+1]
				currentList = [lastDay, currentDate, nextDay]

				#currentList = [priceDates[i-3], priceDates[i-2], priceDates[i-1], priceDates[i], priceDates[i+3], priceDates[i+2], priceDates[i+1]]
				weekPrices = [prices[i-3], prices[i-2], prices[i-1], prices[i], prices[i+3], prices[i+2], prices[i+1]]




				weekPriceDicts.update({currentDate: weekPrices})
			except Exception as e:
				print(e)
		i+=1

	return weekPriceDicts



#print(btcWeekPrices)


def corrCoefForWeeks(pair1, pair2):
	ccDicts = {}
	btcWeekPriceDict = weekPriceFunc('BtcUsd')
	ethWeekPriceDict = weekPriceFunc('EthUsd')

	dates = []
	for date in btcWeekPriceDict:
		dates.append(date)

	for date in dates:
		btcWeek = btcWeekPriceDict[date]
		ethWeek = ethWeekPriceDict[date]
		currentCC = correlationCoefficient(btcWeek, ethWeek)[0][1]
		ccDicts.update({date: currentCC})

	return ccDicts

btcEthCC = corrCoefForWeeks('BtcUsd', 'EthUsd')


def plotCC(pair1, pair2):
	ccWeeks = corrCoefForWeeks(pair1, pair2)
	dates = list(ccWeeks.keys())
	fDates = []
	for date in dates:
		splitDate = date.split(" ")
		fDate = splitDate[0]
		fDates.append(fDate)



	ccs = list(ccWeeks.values())

	print(dates)
	print(ccs)

	#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=20))


	plt.plot(fDates, ccs)

	plt.gcf().autofmt_xdate()

	plt.title('BTC/ETH Correlation Coefficient')


	plt.show()

plotCcBtcEth = plotCC('BtcUsd', 'EthUsd')




echoDtOutput = echoDt('Completed', "Correlation Coefficient")
