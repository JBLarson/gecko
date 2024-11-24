

from geckoFuncz import *
import numpy as np
import pandas as pd



# lambda funcs

ro1, ro2, ro4, ro6, ro8 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4), lambda x : round(x, 6), lambda x : round(x, 8)


ccDict = readJsonFunc('data/cc.json')
geckoData = readJsonFunc('data/gData.json')


#print(ccDict)
#print('\n\nEnd of raw data\n')


cc30 = ccDict['30']
cc90 = ccDict['90']
cc180 = ccDict['180']
cc365 = ccDict['365']

def preLoadCC(inputCC):

	newCC = {}

	#print(inputCC)
	ccKeys = list(inputCC.keys())
	for ccKey in ccKeys:
		ccKey0 = ccKey.lower()
		newKey = ccKey0[:-3]
	
		newCC.update({newKey:inputCC[ccKey]})

	outputCC = {1: None}



	return newCC


#pcc90 = preLoadCC(cc90)

pcc30, pcc90 = preLoadCC(cc30), preLoadCC(cc90)
pcc180, pcc365 = preLoadCC(cc180), preLoadCC(cc365)

print('\nOutput\n')
print(pcc90)



print('\nComplete\n')



def loadCCPandas(inputCC):

	ccDf = pd.DataFrame(inputCC)
	ccData = []
	cryptoKeys = list(inputCC.keys())

	for key in cryptoKeys:
		#print(key)
		currentCrypto = inputCC[key]
		#print(currentCrypto)

	return ccDf






cc30Df, cc90Df = loadCCPandas(pcc30), loadCCPandas(pcc90)
cc180Df, cc365Df = loadCCPandas(pcc180), loadCCPandas(pcc365)

# create dfList - data structure subject to change
dfList = [cc30Df, cc90Df, cc180Df, cc365Df]
df90, df180 = dfList[1], dfList[2]






'''
def analyzeDf(inputDf, inputCC):
	#for currentDf in inputDfLi:
	print('\nRaw CC')
	print(inputCC)
	print('\n\n')
	print(inputDf.describe())

	print('\nMean')

	print(inputDf.mean())




dfAnalysis = analyzeDf(df90, cc90)
print('\nOutput\n')
print(dfAnalysis)



'''


def analyzeDf2(inputDf, geckoData):
	#for currentDf in inputDfLi:
	geckoDf = pd.DataFrame(geckoData)
	print('\nRaw geckoDf')
	print(geckoDf)
	print('\n\n')
	print(inputDf.describe())

	print('\nMean')

	print(inputDf.mean())





dfAnalysis2 = analyzeDf2(df90, geckoData)
print('\nOutput\n')
print(dfAnalysis2)


