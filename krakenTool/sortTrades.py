#! /usr/bin/python

from datetime import datetime, timedelta, date
from time import strftime, strptime, mktime
import json

#previously called readGekko for reasons beyond me

# create time variables
time = datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nSorting Trades on: " + str(justDate) + " at: " + str(justTime) + "\n")

# rounding lambdas
ro1, ro2, ro4, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4), lambda x : round(x, 8)



# import trade data
krakenInAddr = 'data/trades.json'

with open(krakenInAddr, 'r') as f:
	tradeData = json.load(f)


# sort into buy and sell
buyTrades, sellTrades = [], []
for trade in tradeData:
	if trade['type'] == 'sell':
		sellTrades.append(trade)

	elif trade['type'] == 'buy':
		buyTrades.append(trade)



def standardizeSymbols(symbol):
	if symbol.upper() == 'XETHZ':	symbol = 'ETH'
	#if symbol.upper() == 'DAI':	symbol = 'USD'
	if symbol.upper() == 'XBT':	symbol = 'BTC'
	if symbol.upper() == 'XXBTZ':	symbol = 'BTC'
	if symbol.upper() == 'XXMRZ':	symbol = 'XMR'
	return symbol




def tradeQuoteFunc(tradeDataSet):
	tradeQuotes = {}
	for trade in tradeDataSet:
		tradeQuote = trade['quote']
		tradeBase = trade['base']

		tradeBase = standardizeSymbols(tradeBase)
		tradeQuote = standardizeSymbols(tradeQuote)

		trade['quote'] = tradeQuote
		trade['base'] = tradeBase

		if tradeQuote not in tradeQuotes.keys():
			tradeQuotes.update({tradeQuote: []})

	return tradeQuotes

buyQuotes = tradeQuoteFunc(buyTrades)
sellQuotes = tradeQuoteFunc(sellTrades)



def tradeSort(tradeData, tradeQuotes):
	for trade in tradeData:
		currentTradeQuote = trade['quote']
		for matchQuote in tradeQuotes.keys():
			if matchQuote == currentTradeQuote:
				tradeQuotes[matchQuote].append(trade)

	return tradeQuotes



sortedBuys = tradeSort(buyTrades, buyQuotes)
sortedSells = tradeSort(sellTrades, sellQuotes)


exportDict = {"buy": sortedBuys, "sell": sortedSells}




jsonOutAddr = 'data/sortedTrades.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(exportDict, fp1)

	print("\nSuccess Creating Sorted Trade JSON file at: " + str(jsonOutAddr) + '\n')


except Exception as e: print(e)

