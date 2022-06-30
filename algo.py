


from geckoFuncz import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




#lambda functions for rounding
ro1, ro2, ro4, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4), lambda x : round(x, 6), lambda x : round(x, 8)



geckoData = readJsonFunc('data/gData2.json')



targetData = geckoData['KavaUsd']

#print(ethData.keys())


# find differences between moving avgs
def maDiff(JB3USD):
	pChange = JB3USD['pChange']
	priceData = JB3USD['data']
	dateList = list(pChange.keys())

	ma3, ma7, ma14, ma30, ma50, ma90, ma200 = JB3USD['movingAvg3'], JB3USD['movingAvg7'], JB3USD['movingAvg14'], JB3USD['movingAvg30'], JB3USD['movingAvg50'], JB3USD['movingAvg90'], JB3USD['movingAvg200']

	madDictList = []
	for dateKey in dateList[0:]:
		madDict = {'date': dateKey, 'd3_7': None, 'd3_14': None, 'd3_30': None,
				   'd3_50': None, 'd3_90': None, 'd3_200': None, 'd7_14': None,
				   'd7_30': None, 'd7_50': None, 'd7_90': None, 'd7_200': None,
				   'd14_30': None, 'd14_50': None, 'd14_90': None, 'd14_200': None,
				   'd30_50': None, 'd30_90': None, 'd30_200': None, 'd50_90': None,
				   'd50_200': None, 'd90_200': None, 'pChange': None, 'price': None,
				   'pair': JB3USD['pair']
				   }

		
		# current moving avg variable
		c3, c7, c14, c30, c50, c90, c200 = ma3[dateKey], ma7[dateKey], ma14[dateKey], ma30[dateKey], ma50[dateKey], ma90[dateKey], ma200[dateKey]


		# difference variables
		d3_7, d3_14, d3_30, d3_50, d3_90, d3_200 = ro2((c3 - c7)/c7), ro2((c3 - c14)/c14), ro2((c3 - c30)/c30), ro2((c3 - c50)/c50), ro2((c3 - c90)/c90), ro2((c3 - c200)/c200)


		d7_14, d7_30, d7_50, d7_90, d7_200, d14_30  = ro2((c7 - c14)/c14), ro2((c7 - c30)/c30), ro2((c7 - c50)/c50), ro2((c7 - c90)/c90), ro2((c7 - c200)/c200), ro2((c14 - c30)/c30)

		d14_50, d14_90, d14_200, d30_50, d30_90, d30_200  = ro2((c14 - c50)/c50), ro2((c14 - c90)/c90), ro2((c14 - c200)/c200), ro2((c30 - c50)/c50), ro2((c30 - c90)/c90), ro2((c30 - c200)/c200)

		
		d50_90, d50_200, d90_200 = ro2((c50 - c90)/c90), ro2((c50 - c200)/c200), ro2((c90 - c200)/c200)
		currentPrice, currentPchange = ro2(priceData[dateKey]), ro4(pChange[dateKey])

		#print(d7_30)


		madDict['d3_7'], madDict['d3_14'], madDict['d3_30'], madDict['d3_50'], madDict['d3_90'], madDict['d3_200'] = d3_7, d3_14, d3_30, d3_50, d3_90, d3_200

		madDict['d7_14'], madDict['d7_30'], madDict['d7_50'], madDict['d7_90'], madDict['d7_200'] = d7_14, d7_30, d7_50, d7_90, d7_200
		madDict['d14_30'], madDict['d14_50'], madDict['d14_90'], madDict['d14_200'] = d14_30, d14_50, d14_90, d14_200
		madDict['d30_50'], madDict['d30_90'], madDict['d30_200'] = d30_50, d30_90, d30_200
		madDict['d50_90'], madDict['d50_200'], madDict['d90_200'] = d50_90, d50_200, d90_200
		madDict['pChange'], madDict['price'] = currentPchange, currentPrice


		#print(madDict)



		madDictList.append(madDict)


	return madDictList



targetMaDiff = maDiff(targetData)



def plotMAdiff(maDiffList):
	
	priceList, dateList = [], []
	maPlotList3, maPlotList4, maPlotList5 = [], [], []
	maPlotList0, maPlotList1, maPlotList2 = [], [], []

	countVar = 0
	currentPair = ''
	for maData in maDiffList:
		#print('\n')

		dateList.append(maData['date'])
		priceList.append(maData['pChange'])
		maPlotList0.append(maData['d7_30'])
		maPlotList1.append(maData['d7_50'])
		maPlotList2.append(maData['d7_200'])
		maPlotList3.append(maData['d30_50'])
		maPlotList4.append(maData['d30_200'])
		maPlotList5.append(maData['d50_200'])


		maVariable = maData['pChange']

		maVariable = maVariable


		if maVariable < 0:
			print(ro4(maVariable))
			countVar += 1
			currentPair = maData['pair']
			print(str(maData['date']) + '   $' + str(maData['price']) + '   ' +str(maData['d7_30']) + '   ' + str(maData['d7_50']) + '   ' + str(maData['d7_200']))

	countPct = ro2(100-((len(maDiffList)-countVar)/len(maDiffList))*100)
	print('\nNumber of records: ' + str(countVar) + '   ' + str(countPct) + '%')
	print(len(maDiffList))


	'''

	figure, axis = plt.subplots(1, 1)



	axis.plot(dateList, priceList, label="price")

	axis.plot(dateList, maPlotList0, label="d7_30")
	#axis.plot(dateList, maPlotList1, label="d7_50")
	axis.plot(dateList, maPlotList2, label="d7_200")
	#axis.plot(dateList, maPlotList3, label="d30_50")
	#axis.plot(dateList, maPlotList4, label="d30_200")
	axis.plot(dateList, maPlotList5, label="d50_200")


	plotTitle = str(currentPair) + "  -  Moving Average Variance"
	axis.set_title(plotTitle)


	plt.legend()

	plt.show()

	'''

plotEth = plotMAdiff(targetMaDiff)


for maMath in targetMaDiff[-5:]:
	print('\n')
	#print(maMath)
	currentKeys = list(maMath.keys())
	for mKey in currentKeys:
		print(str(mKey) + '   ' + str(maMath[mKey]))

