
   
#!/usr/bin/python3

from geckoFuncz import readJsonFunc, createJsonFunc, echoDt, nDayFunc
import numpy as np


echoDtOutput = echoDt('Started', "Correlation Coefficient")




#lambda functions for rounding
ro1, ro2, ro4, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4), lambda x : round(x, 6), lambda x : round(x, 8)




geckoData = readJsonFunc('data/analyzeAll.json')
geckoKeys = list(geckoData.keys())




def correlationCoefficient(list1, list2):
	corrCoef = np.corrcoef(list1, list2)
	return corrCoef



def allMovingCorrCoefFunc(geckoKey, n):
	corrCoefOutput = {}
	tokenPrices = list(geckoData[geckoKey]['pChange'].values())[-n-1: -1]


	for key in geckoKeys:
		comparisonToken = list(geckoData[key]['pChange'].values())[-n-1: -1]

		comparisonCorrCoef = ro4(float(correlationCoefficient(comparisonToken, tokenPrices)[0,1]))
		corrCoefOutput.update({key: comparisonCorrCoef})


	return corrCoefOutput



cc7, cc30, cc200 = {}, {}, {}

for geckoKey in geckoKeys:
	corrCoef7 = allMovingCorrCoefFunc(geckoKey, 7)
	corrCoef30 = allMovingCorrCoefFunc(geckoKey, 30)
	corrCoef200 = allMovingCorrCoefFunc(geckoKey, 200)


	cc7.update({geckoKey: corrCoef7})
	cc30.update({geckoKey: corrCoef30})
	cc200.update({geckoKey: corrCoef200})


coorCoefs = {7: cc7, 30: cc30, 200: cc200}


saveCC = createJsonFunc('data/cc.json', coorCoefs)

print(saveCC)

echoDtOutput = echoDt('Completed', "Correlation Coefficient")
