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
jsonInAddr = 'data/geckoAnalysis2.json'
with open(jsonInAddr, 'r') as f:
	geckoData = json.load(f)




def plotTokenFunc(tokenSymbol, startDateIndex, endDateIndex):
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


def getDouble(self):
    d, okPressed = QInputDialog.getDouble(self,"Date Range","Value:", 30, 0, 100, 1)
    if okPressed:
        global sdi
        sdi = int(-d)
        print("Date range(#): " + str(d))

#sdi, edi = -90, -1
edi = -1

def window():
	app = QApplication(sys.argv)
	win = QDialog()

	getDouble(win)

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
	pltBtcUsd = plotTokenFunc('BtcUsd', sdi, edi)

def plotBtcEur():
	pltBtcEur = plotTokenFunc('BtcEur', sdi, edi)

def plotEthUsd():
	pltEthUsd = plotTokenFunc('EthUsd', sdi, edi)

def plotEthEur():
	pltEthEur = plotTokenFunc('EthEur', sdi, edi)


def plotDaiUsd():
	pltDaiUsd = plotTokenFunc('DaiUsd', sdi, edi)

def plotDaiEur():
	pltDaiEur = plotTokenFunc('DaiEur', sdi, edi)


def plotAdaUsd():
	pltAdaUsd = plotTokenFunc('AdaUsd', sdi, edi)

def plotAdaEur():
	pltAdaEur = plotTokenFunc('AdaEur', sdi, edi)

def plotLinkUsd():
	pltLinkUsd = plotTokenFunc('LinkUsd', sdi, edi)

def plotLinkEur():
	pltLinkEur = plotTokenFunc('LinkEur', sdi, edi)


def plotXmrUsd():
	pltXmrUsd = plotTokenFunc('XmrUsd', sdi, edi)

def plotXmrEur():
	pltXmrEur = plotTokenFunc('XmrEur', sdi, edi)


if __name__ == '__main__':
	window()

