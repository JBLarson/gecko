#!/usr/bin/python3


import sys
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




def plotTokenFunc(tokenSymbol, startDateIndex):
	tokenPair = geckoData[tokenSymbol]
	tokenPairMovingAvg7 = tokenPair['movingAvg7']
	tokenPairMovingAvg30 = tokenPair['movingAvg30']
	tokenPairMovingAvg50 = tokenPair['movingAvg50']
	tokenPairMovingAvg200 = tokenPair['movingAvg200']

	tokenPairPrices = tokenPair['data']
	tokenPairStdDev = tokenPair['stdDev']
	tokenPairVolume = tokenPair['volumeData']

	movingAvgKeys = list(tokenPairMovingAvg30.keys())


	smaDates, sma7Prices, sma30Prices, sma50Prices, sma200Prices, prices, volumes = [], [], [], [], [], [], []

	for key in movingAvgKeys[startDateIndex:]:
		smaDates.append(key)
		sma7Prices.append(tokenPairMovingAvg7[key])
		sma30Prices.append(tokenPairMovingAvg30[key])
		sma50Prices.append(tokenPairMovingAvg50[key])
		sma200Prices.append(tokenPairMovingAvg200[key])

		prices.append(tokenPairPrices[key])
		volumes.append(tokenPairVolume[key])


	#plt.subplot(211)



	plt.plot(smaDates, prices, label="Price")
	plt.plot(smaDates, sma7Prices, label="7-Day SMA")


	plt.plot(smaDates, sma30Prices, label="30-Day SMA")
	plt.plot(smaDates, sma50Prices, label="50-Day SMA")

	plt.plot(smaDates, sma200Prices, label="200-Day SMA")

	plt.ylabel('Price')

	priceTitle = tokenSymbol + " Prices and SMA"
	plt.title(priceTitle)
	plt.legend()
	plt.show()


geckoKeys = geckoData.keys()

print("\nAvailable Pairs: " + str(geckoKeys) + "\n")

userInput = False
#userInput = True

# create infinite loop - after a chart is closed the user can enter a new time-frame / token
i = 0
if userInput == True:
	while i < 2:
		sdiInput = -int(input("Number of days in sample: "))
		tokenInput = input("Token Pair: ")

		plotToken = plotTokenFunc(tokenInput, sdiInput)


#plotTokenTest = plotTokenFunc('AdaUsd', 180)


def fetchPairData(tokenSymbol):
	tokenData = geckoData[tokenSymbol]
	tokenDataList = [tokenData['data'], tokenData['movingAvg7'], tokenData['movingAvg30']]
	return tokenDataList


def plotToken2Func(tokenSymbol0, tokenSymbol1, startDateIndex):

	token0Data = geckoData[tokenSymbol0]
	token1Data = geckoData[tokenSymbol1]
	token0Prices, token0MA7, token0MA30 = token0Data['data'], token0Data['movingAvg7'], token0Data['movingAvg30']
	token1Prices, token1MA7, token1MA30 = token1Data['data'], token1Data['movingAvg7'], token1Data['movingAvg30']

	dateKeys = list(token0Prices.keys())

	dates = []
	t0MA7, t0MA30, t0Prices = [], [], []
	t1MA7, t1MA30, t1Prices = [], [], []


	for key in dateKeys[startDateIndex:]:
		dates.append(key)
		t0Prices.append(token0Prices[key])
		t0MA7.append(token0MA7[key])
		t0MA30.append(token0MA30[key])

		t1Prices.append(token1Prices[key])
		t1MA7.append(token1MA7[key])
		t1MA30.append(token1MA30[key])



	#plt.subplot(211)



	plt.plot(dates, t0Prices, label=str(tokenSymbol0))
	plt.plot(dates, t0MA7, label=str(tokenSymbol0) + " 7Day MA")
	plt.plot(dates, t0MA30, label=str(tokenSymbol0) + " 30Day MA")

	plt.plot(dates, t1Prices, label=str(tokenSymbol1))
	plt.plot(dates, t1MA7, label=str(tokenSymbol1) + " 7Day MA")
	plt.plot(dates, t1MA30, label=str(tokenSymbol1) + " 30Day MA")



	plt.ylabel('Price')

	priceTitle = tokenSymbol0 + " & " + tokenSymbol1 + " Prices and SMA"
	plt.title(priceTitle)
	plt.legend()
	plt.show()


plotToken2Test = plotToken2Func('AdaUsd', 'AdaEur', 180)
