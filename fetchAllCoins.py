#!/usr/bin/python3

import time
import datetime
import json





def getCoins(baseCurrency):
	from pycoingecko import CoinGeckoAPI
	cg = CoinGeckoAPI()

	coinApiRez = cg.get_coins_markets(vs_currency=baseCurrency)
	
	#for tokenData in coinApiRez:
	#	print(tokenData)
	#coinRezPrices = coinApiRez['prices']
	#coinRezVolumes = coinApiRez['total_volumes']


	return coinApiRez



geckoData = getCoins('usd')




symbolNames = {}

for tokenDict in geckoData:
	tokenSymbol = tokenDict['symbol']
	#print(tokenSymbol)
	tokenName = tokenDict['name']
	tokenId = tokenDict['id']
	symbolName = {tokenId: tokenName}
	symbolNames.update(symbolName)

print(symbolNames)

writeSymbolNames = createJsonFunc('data/allSymbols.json', symbolNames)
print(writeSymbolNames)



