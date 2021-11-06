
import pandas as pd
import json
import csv

# import CSV file

tradesInAddr = 'data/sampleTrades.csv'
tradesData = pd.read_csv(tradesInAddr)

# create pandas series from pandas dataframe
tradePairs = (tradesData['pair'])
tradePrices = (tradesData['price'])
tradeCost = (tradesData['cost'])
tradeFees = (tradesData['fee'])
tradeDates = (tradesData['date'])

tradeTimes = (tradesData['time'])
tradeTypes = tradesData['type']
tradeVolumes = tradesData['vol']




def standardizeSymbols(symbol):
	if symbol.upper() == 'XETHZ':	symbol = 'ETH'
	#if symbol.upper() == 'DAI':	symbol = 'USD'
	if symbol.upper() == 'XBT':	symbol = 'BTC'
	if symbol.upper() == 'XXBTZ':	symbol = 'BTC'
	if symbol.upper() == 'XXMRZ':	symbol = 'XMR'
	return symbol





tradePairz = []
try:
	for i in range(tradePairs.shape[0]):

		tradePair = {'order': i, 'quote': '', 'base': '', 'dateTime': '', 'date': '','time': '',
					 'price': '', 'volume': '', 'cost': '', 'type': '', 'usdCost': '',
					 'histQuote': '', 'histBase': ''}

		# datetime object		
		ttime = tradeTimes[i]
		tdate = tradeDates[i]
		tdtime = str(tdate) + ' ' + str(ttime)
		#print(tdtime)

		tradePair['dateTime'] = tdtime
		tradePair['date'] = tdate
		tradePair['time'] = ttime
		
		#price, cost, fee, type and volume
		tfee = tradeFees[i]
		tprice = tradePrices[i]
		tcost = tradeCost[i]
		tvolume = tradeVolumes[i]
		ttype = tradeTypes[i]

		tradePair['fee'] = tfee
		tradePair['price'] = tprice
		tradePair['cost'] = tcost
		tradePair['type'] = ttype
		tradePair['volume'] = tvolume



		#parse currency pair
		pair = tradePairs[i]

		if 'USD' in pair[3:]:
			tradePair2 = pair.split('USD')
			tradePair['base'] = 'USD'
			tradePair['quote'] = standardizeSymbols(tradePair2[0])

		if 'EUR' in pair[3:]:
			tradePair2 = pair.split('EUR')
			tradePair['base'] = 'EUR'
			tradePair['quote'] = standardizeSymbols(tradePair2[0])

		if 'DAI' in pair[3:]:
			tradePair2 = pair.split('DAI')
			tradePair['base'] = 'DAI'
			tradePair['quote'] = standardizeSymbols(tradePair2[0])

		if 'ETH' in pair[3:]:
			tradePair2 = pair.split('ETH')
			tradePair['base'] = 'ETH'
			tradePair['quote'] = standardizeSymbols(tradePair2[0])

		if 'ADA' in pair[3:]:
			tradePair2 = pair.split('ADA')
			tradePair['base'] = 'ADA'
			tradePair['quote'] = standardizeSymbols(tradePair2[0])

		if 'XBT' in pair[3:]:
			tradePair2 = pair.split('XBT')
			tradePair['base'] = 'BTC'
			tradePair['quote'] = standardizeSymbols(tradePair2[0])

		tradePairz.append(tradePair)


except Exception as e:	print(e)



jsonOutAddr = 'data/trades.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(tradePairz, fp1)

	print("\nSuccess Creating JSON file for: " + str(len(tradePairz)) + ' trades')


except Exception as e: print(e)


