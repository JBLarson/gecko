#!/usr/bin/python3


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import time
import datetime
import dateparser
import json
import math
import matplotlib.pyplot as plt

#lambda functions for rounding
ro1, ro2, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 6), lambda x : round(x, 8)


# import coinGecko data
jsonInAddr = 'data/geckoAnalysis3.json'
with open(jsonInAddr, 'r') as f:
	geckoData = json.load(f)


def plotTokenFuncOG(tokenSymbol):
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


def plotTokenFunc(tokenSymbol):
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

	for key in movingAvgKeys:
		smaDates.append(key)
		sma7Prices.append(tokenPairMovingAvg7[key])
		sma30Prices.append(tokenPairMovingAvg30[key])
		sma50Prices.append(tokenPairMovingAvg50[key])
		sma200Prices.append(tokenPairMovingAvg200[key])

		prices.append(tokenPairPrices[key])
		volumes.append(tokenPairVolume[key])


	plt.plot(smaDates, prices, label="Price")
	plt.plot(smaDates, sma7Prices, label="7-Day SMA")


	plt.plot(smaDates, sma30Prices, label="30-Day SMA")
	plt.plot(smaDates, sma50Prices, label="50-Day SMA")

	#plt.plot(smaDates, sma200Prices, label="200-Day SMA")

	plt.ylabel('Price')

	priceTitle = tokenSymbol + " Prices and SMA"
	plt.title(priceTitle)
	plt.legend()
	plt.show()

def window():
	app = QApplication(sys.argv)
	win = QDialog()
	p1 = QPushButton(win)
	p1.setText("Plot BtcUsd")
	p1.move(20,20)
	p1.clicked.connect(plotBtcUsd)

	p2 = QPushButton(win)
	p2.setText("Plot BtcEur")
	p2.move(20,60)
	p2.clicked.connect(plotBtcEur)
	
	p3 = QPushButton(win)
	p3.setText("Plot EthUsd ")
	p3.move(20,100)
	p3.clicked.connect(plotEthUsd)
	
	p4 = QPushButton(win)
	p4.setText("Plot EthEur")
	p4.move(20,140)
	p4.clicked.connect(plotEthEur)

	p5 = QPushButton(win)
	p5.setText("Plot AdaUsd")
	p5.move(140,20)
	p5.clicked.connect(plotAdaUsd)
	
	p6 = QPushButton(win)
	p6.setText("Plot AdaEur ")
	p6.move(140,60)
	p6.clicked.connect(plotAdaEur)
	
	p7 = QPushButton(win)
	p7.setText("Plot XmrUsd")
	p7.move(140,100)
	p7.clicked.connect(plotXmrUsd)

	p8 = QPushButton(win)
	p8.setText("Plot XmrEur")
	p8.move(140,140)
	p8.clicked.connect(plotXmrEur)
	
	p9 = QPushButton(win)
	p9.setText("Plot LinkUsd ")
	p9.move(260,20)
	p9.clicked.connect(plotLinkUsd)
	
	p10 = QPushButton(win)
	p10.setText("Plot LinkEur")
	p10.move(260,60)
	p10.clicked.connect(plotLinkUsd)

	p11 = QPushButton(win)
	p11.setText("Plot DaiUsd")
	p11.move(260,100)
	p11.clicked.connect(plotDaiUsd)
	
	p12 = QPushButton(win)
	p12.setText("Plot DaiEur ")
	p12.move(260,140)
	p12.clicked.connect(plotDaiEur)
	


	win.setGeometry(800,100,400,200)

	win.setWindowTitle("Plot - Gecko")
	win.show()
	sys.exit(app.exec_())




def plotBtcUsd():
	pltBtcUsd = plotTokenFunc('BtcUsd')

def plotBtcEur():
	pltBtcEur = plotTokenFunc('BtcEur')

def plotEthUsd():
	pltEthUsd = plotTokenFunc('EthUsd')

def plotEthEur():
	pltEthEur = plotTokenFunc('EthEur')

def plotDaiUsd():
	pltDaiUsd = plotTokenFunc('DaiUsd')

def plotDaiEur():
	pltDaiEur = plotTokenFunc('DaiEur')

def plotAdaUsd():
	pltAdaUsd = plotTokenFunc('AdaUsd')

def plotAdaEur():
	pltAdaEur = plotTokenFunc('AdaEur')

def plotLinkUsd():
	pltLinkUsd = plotTokenFunc('LinkUsd')

def plotLinkEur():
	pltLinkEur = plotTokenFunc('LinkEur')

def plotXmrUsd():
	pltXmrUsd = plotTokenFunc('XmrUsd')

def plotXmrEur():
	pltXmrEur = plotTokenFunc('XmrEur')


if __name__ == '__main__':
	window()
