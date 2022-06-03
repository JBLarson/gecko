#!/home/dolores/Desktop/gecko/gEnv/bin/python3

import json
from tFuncs import *


currentPositions = readJsonFunc("positions.json")

#print(currentPositions)
currentPositionSymbols = list(currentPositions.keys())
print('\nContents of currentPositons.json')

print(currentPositions)


def buyTrade(symbol, qty, price):

	cost = qty*price

	print('\nBuying: ' + str(qty) + ' ' + str(symbol) + ' at: $' + str(price) + ' total cost: $' + str(cost))


	if symbol in currentPositionSymbols:
		existingPosition = currentPositions[symbol]
		existingPosition['qty'] += qty
		existingPosition['cost'] += cost

		#print(existingPosition)


	# create trade dict to return
	tradeDict = {"symbol": symbol, "qty": existingPosition['qty'], "cost": existingPosition['cost']}



	return tradeDict



buyTrade = buyTrade('kava', 200, 3)
print('\nNew current position')
print(buyTrade)


# update the master current position object
currentPositions[buyTrade['symbol']].update({"qty": buyTrade["qty"]})


print('\nCurrent positions object: ' + str(currentPositions))
print('\n')

# add the create json func
