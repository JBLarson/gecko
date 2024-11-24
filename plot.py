#!/usr/bin/python3


import sys
import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

import numpy as np
from datetime import datetime


#lambda functions for rounding
ro1, ro2, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 6), lambda x : round(x, 8)


plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format as 'Year-Month-Day'
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Show major ticks for each month

plt.gcf().autofmt_xdate()  # Auto-rotate the dates for better readability


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
		date_obj = datetime.strptime(key, "%Y-%m-%d")

		smaDates.append(date_obj)
		sma7Prices.append(tokenPairMovingAvg7[key])
		sma30Prices.append(tokenPairMovingAvg30[key])
		sma50Prices.append(tokenPairMovingAvg50[key])
		sma200Prices.append(tokenPairMovingAvg200[key])

		prices.append(tokenPairPrices[key])
		volumes.append(tokenPairVolume[key])

	print(smaDates[0])
	print(smaDates[-1])
	print(smaDates[-1:])
	plotDates = []
	for i in range(1, 9):
		if i == 1:
			plotDates.append(smaDates[0])
		elif i != 1:
			i = i - 1
			nextDateIndex = round((i*(len(smaDates)/7)), 0)
			nextDate = smaDates[int(nextDateIndex-1)]
			plotDates.append(nextDate)

	#dates = drange(smaDates[0], smaDates[-1], drange)



	indexList, plotZeroList = [], []
	for i in range(len(smaDates)):	indexList.append(i)

	for i in range(len(plotDates)):	plotZeroList.append(0)

	plt.plot(smaDates, prices, label="Price")
	plt.plot(smaDates, sma7Prices, label="7-Day SMA")
	plt.plot(smaDates, sma30Prices, label="30-Day SMA")
	plt.plot(smaDates, sma50Prices, label="50-Day SMA")
	plt.plot(smaDates, sma200Prices, label="200-Day SMA")
	

	#plt.plot(plotDates, plotZeroList)

	plt.ylabel('Price')

	priceTitle = tokenSymbol + " Prices and SMA"
	plt.title(priceTitle)
	plt.legend()
	plt.show()


def getDouble(self):
	d, okPressed = QInputDialog.getDouble(self,"Date Range","Value:", 180, 0, 365, 0)
	if okPressed:
		global sdi
		sdi = int(-d)
	return sdi
#sdi, edi = -90, -1
edi = -1

def window():
	app = QApplication(sys.argv)
	win = QDialog()
	currentSdi = getDouble(win)

	# buttons for pairs
	p1 = QPushButton(win)
	p1.setText("Plot BtcUsd")
	p1.move(20,40)
	p1.clicked.connect(plotBtcUsd)

	p3 = QPushButton(win)
	p3.setText("Plot EthUsd ")
	p3.move(20,120)
	p3.clicked.connect(plotEthUsd)
	
	p5 = QPushButton(win)
	p5.setText("Plot KavaUsd")
	p5.move(140,40)
	p5.clicked.connect(plotKavaUsd)

	p7 = QPushButton(win)
	p7.setText("Plot XmrUsd")
	p7.move(140,120)
	p7.clicked.connect(plotXmrUsd)

	p9 = QPushButton(win)
	p9.setText("Plot AtomUsd ")
	p9.move(260,40)
	p9.clicked.connect(plotAtomUsd)

	p11 = QPushButton(win)
	p11.setText("Plot DaiUsd")
	p11.move(260,120)
	p11.clicked.connect(plotDaiUsd)
	
	p13 = QPushButton(win)
	p13.setText("Close Chart ")
	p13.move(200,200)
	p13.clicked.connect(closeFig)
	
	p14 = QPushButton(win)
	p14.setText("Quit GUI ")
	p14.move(100,200)
	p14.clicked.connect(quitPlot)


	win.setGeometry(800,100,400,300)

	win.setWindowTitle(str(abs(currentSdi)) + "-day Plot - Gecko")
	win.show()
	sys.exit(app.exec_())


# button function
# control functions
def quitPlot():
	sys.exit()

def closeFig():
	plt.close()


# functions for pairs
def plotBtcUsd():
	pltBtcUsd = plotTokenFunc('BtcUsd', sdi, edi)

def plotEthUsd():
	pltEthUsd = plotTokenFunc('EthUsd', sdi, edi)


def plotDaiUsd():
	pltDaiUsd = plotTokenFunc('DaiUsd', sdi, edi)


def plotKavaUsd():
	pltAdaUsd = plotTokenFunc('KavaUsd', sdi, edi)

def plotAtomUsd():
	pltLinkUsd = plotTokenFunc('AtomUsd', sdi, edi)


def plotXmrUsd():
	pltXmrUsd = plotTokenFunc('XmrUsd', sdi, edi)



if __name__ == '__main__':
	window()
