import json


# import kraken data
sortedTradesInAddr = 'data/sortedTrades.json'

with open(sortedTradesInAddr, 'r') as r:
	tradeData = json.load(r)



sortedSells, sortedBuys = tradeData['sell'], tradeData['buy']


# import coinGecko data
jsonInAddr = 'data/cryptoData.json'

with open(jsonInAddr, 'r') as f:
	gekkoData = json.load(f)

gekkoKeys =gekkoData.keys()


def gekkoPairFunc(gekkoKeys):
	gekkoDicts = []

	for key in gekkoKeys:
		gekkoDict = {}
		if 'Usd' in key:
			splitKey = key.split('Usd')
			keyQuote = splitKey[0]
			keyBase = 'Usd'
		if 'Eur' in key:
			splitKey = key.split('Eur')
			keyQuote = splitKey[0]
			keyBase = 'Eur'

		gekkoDict = {'pair': key, 'quote': keyQuote, 'base': keyBase}
		gekkoDicts.append(gekkoDict)

	return gekkoDicts

gekkoPairs = gekkoPairFunc(gekkoKeys)



def mdyToYMD(ogDate):
	ogDateSplit = ogDate.split("/")
	if len(ogDateSplit[0]) == 1:	month = '0' + str(ogDateSplit[0])
	else:	month = ogDateSplit[0]
	if len(ogDateSplit[1]) == 1:	day = '0' + str(ogDateSplit[1])
	else:	day = ogDateSplit[1]
	if len(ogDateSplit[2]) == 2:	year = '20' + str(ogDateSplit[2])
	else:	year = ogDateSplit[2]


	ymdOutput = str(year) + '-' + str(month) + '-' + str(day)
	return ymdOutput




def getPairPrice(quote, base, targetDate):
	pair = str(quote.capitalize()) + str(base.capitalize())
	targetPrice = "Couldn't find date"

	pairData = gekkoData[pair]
	pairData = pairData['data']
	for dailyData in pairData:
		dailyDateShort = dailyData[:10]
		#print((dailyDateShort))
		#print((targetDate))
		if dailyDateShort != targetDate:
			pass
		elif dailyDateShort == targetDate:
			targetPrice = pairData[dailyData]
	return targetPrice












def priceTradeList(sortedTradeData):
	symbolList = []
	tradeKeys = sortedTradeData.keys()
	for key in tradeKeys:
		if key == "XETHZ":	key = "ETH"
		if key == "XXBTZ":	key = "BTC"
		if key == "XXMRZ":	key = "XMR"

		symbolList.append(key)
	return symbolList




#priceBuyOrders = priceTradeList(sortedBuys)

#print(priceBuyOrders)

#print("\nSell orders")
#priceSellOrders = priceTradeList(sortedSells)


#ethBuys = sortedBuys['ETH']

#for ethBuy in ethBuys:
#	print(ethBuy)
gekkoPairValueList = []
for gekkoPair in gekkoPairs:
	gekkoPairValue = gekkoPair['pair']
	gekkoPairValueList.append(gekkoPairValue)



def getHistSymbolPrice(tradeSymbol, tradeDate):
	symbolUsdPair = str(tradeSymbol).capitalize() + str('Usd')
	try:
		histSymbol = gekkoData[symbolUsdPair]['data'][tradeDate]

	except Exception as e:
		print("Error finding historical data for: " + str(tradeSymbol))
		print("Error msg: " + str(e))
		histSymbol = 'histPrice error'
	
	return histSymbol


# need to seperate histQuote and histBase functions
def sortingFunction(sortedTradeData):
	tradeList, symbolList = [], {}

	tradeKeys = sortedTradeData.keys()

	for key in tradeKeys:
		keyTradeData = sortedTradeData[key]
		#print("\n\nTrades for: " + str(key))
		for trade in keyTradeData:
			tradeDate = mdyToYMD(trade['date'])
			tradeDate = str(tradeDate)
			tradeBase = trade['base'].capitalize()
			tradeQuote = trade['quote'].capitalize()
			pair = trade['quote'].capitalize() + tradeBase
			

			if pair in gekkoPairValueList:

				currentHistData = gekkoData[pair]
				currentTrade = currentHistData['data']
				currentHistQuote = currentTrade[tradeDate]
				trade['histQuote'] = currentHistQuote
				tradeList.append(trade)
			elif pair not in gekkoPairValueList:
				print("Pair not in gekkoPairs: " +str(pair))
				tradeList.append(trade)



	return tradeList

		#currentTradeList = sortedTradeData[trade]

	#return currentTradeList

print("\nSell orders")

sortedBuyOrders = sortingFunction(sortedBuys)




sortedSellOrders = sortingFunction(sortedSells)



print("\n\nFunc Output")



def quoteBaseFunc(sortedOrders):
	pricedSortedOrders = []
	for order in sortedOrders:
		

		orderBase = order['base']
		orderQuote = order['quote']
		orderDate = mdyToYMD(order['date'])
		orderHistQuote = order['histQuote']

		if orderBase != 'USD' and orderBase != 'EUR':

			histPrice = getHistSymbolPrice(orderBase, orderDate)
			order['histBase'] = histPrice

		if orderHistQuote == '':

			histPrice = getHistSymbolPrice(orderQuote, orderDate)
			order['histQuote'] = histPrice


		pricedSortedOrders.append(order)
	return pricedSortedOrders


pricedSortedSells = quoteBaseFunc(sortedSellOrders)
pricedSortedBuys = quoteBaseFunc(sortedBuyOrders)





print("\n\nBuy Trades")

for trade in pricedSortedBuys:
	print("\n\n")
	print(trade)

print("\n\nSell Trades")
for trade in pricedSortedSells:
	print("\n\n")
	print(trade)





exportDict = {"buy": pricedSortedBuys, "sell": pricedSortedSells}



jsonOutAddr = 'data/pricedTrades.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(exportDict, fp1)

	print("\nSuccess Creating Sorted Trade JSON file at: " + str(jsonOutAddr) + '\n')


except Exception as e: print(e)




