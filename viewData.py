#!/usr/bin/python3

import json
import math


#lambda functions for rounding
ro1, ro2, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 6), lambda x : round(x, 8)


# import coinGecko data
jsonInAddr = 'data/geckoAnalysis.json'
with open(jsonInAddr, 'r') as f:
	geckoData = json.load(f)



geckoKeys = list(geckoData.keys())
for geckoKey in geckoKeys:
	print("\n" + geckoData[geckoKey]['pair'])
	print("Avg: " + str(geckoData[geckoKey]['avg']))
	print("StdDev: " + str(geckoData[geckoKey]['stdDev']))
	print("Min: " + str(geckoData[geckoKey]['min']))
	print("Max: " + str(geckoData[geckoKey]['max']))


