#!/usr/bin/python3

import time
import datetime
import json
from geckoFuncz import unixToDatetime, datetimeToUnix, analyzeAllTokens, stdDevFunc, pChangeFunc
import ezDT
try:
	from pycoingecko import CoinGeckoAPI
	cg = CoinGeckoAPI()
except:
	print("failed to import coingeckoAPI")


# import symbolName data
symbolNamesInAddr = 'data/allSymbols.json'

with open(symbolNamesInAddr, 'r') as r:
	symbolNameDict = json.load(r)




def oneYearAgo(ogDT):
	splitDT = ogDT.split("-")
	year = splitDT[0]
	
	restOfDt = str(splitDT[1]) +"-" + str(splitDT[2])
	yearMinusOne = int(year) - 1
	oneYearResult = str(yearMinusOne) + "-" + str(restOfDt)
	
	return oneYearResult


today = datetime.datetime.now()
today = str(today).split(".")
today = today[0]
oneYearAgo = oneYearAgo(today)

epochToday = datetimeToUnix(today)
epochOneYearAgo = datetimeToUnix(oneYearAgo)


def lastYearOfDates(todaysDateTime):

	dateList = []

	for i in range(365):
		iDatetime = str(ezDT.subtractDays(todaysDateTime, i))
		iDate = iDatetime.split(" ")[0]
		dateList.append(iDate)

	return dateList


def mdyTodmy(mdyDate):
	splitDT = mdyDate.split("-")
	dmyDate = splitDT[2]+"-"+splitDT[1]+"-"+splitDT[0]
	return dmyDate


lastYearDateList = lastYearOfDates(today)




def readDict(inputDict):
	iDictKeys = list(inputDict.keys())
	for iDictKey in iDictKeys:
		print(str(iDictKey) + " " + str(inputDict[iDictKey]))



def fetchStats(coin, targetDate):
	coinApiRez = cg.get_coin_history_by_id(id=coin, date=targetDate, localization='false') # coin gecko coinApiRez

	communityData = coinApiRez['community_data']
	devData = coinApiRez['developer_data']
	coinStats = {'community': communityData, 'dev': devData}
	return coinStats




# need to replace logic with a time.sleep() function


socialDataDict, rqCount = {}, 0

for targetDate in lastYearDateList:
	if rqCount > 45:
		time.sleep(60)
		rqCount = 0
	else:
		targetDateDMY = mdyTodmy(targetDate)
		print("Fetched data for: " + str(targetDate))
		socialData = fetchStats('cardano', targetDateDMY)
		socialDataDict.update({targetDate: socialData})
	
	rqCount = rqCount + 1





jsonOutAddr = 'data/socialData' + '.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(socialDataDict, fp1)


	print("\nSuccess Creating Crypto Json on/at: " + str(jsonOutAddr) + "\n")

except Exception as e:
	print(e)	
