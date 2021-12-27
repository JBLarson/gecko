#!/usr/bin/python3


import numpy as np
import sys

#lambda functions for rounding
ro1, ro2, ro4, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4), lambda x : round(x, 6), lambda x : round(x, 8)

def tradeDict(price, qty):
	cost = ro4(price * qty)
	outputDict = {'cost': cost, 'price': price, 'qty': qty}
	return outputDict



def exitTrades(inputTrade):
	inputPrice, inputQty = inputTrade['price'], inputTrade['qty']
	inputCost = inputTrade['cost']
	print('\nInput trade cost: ' + str(inputCost) + '\n')

	for exitPrice in np.arange(inputPrice-inputPrice*0.25, inputPrice+inputPrice*0.25, inputPrice/50):
		exitPrice = ro6(exitPrice)
		exitCost = ro4(exitPrice*inputQty)
		profitLoss = ro4(exitCost - inputCost)
		print('Exit Price: ' + str(exitPrice) + '  Value: $' + str(exitCost) + '  P/L: $' + str(profitLoss))
		



inputPrice, inputQty = sys.argv[1], sys.argv[2]
trade0 = tradeDict(inputPrice, inputQty)


print('\nInput trade: ' + str(trade0) + '\n')


exitTradeTest = exitTrades(trade0)

