
import datetime
import json
from geckoFuncz import unixToDatetime, datetimeToUnix
import pycoingecko

# import coinGecko data
jsonInAddr = 'data/gTest.json'

with open(jsonInAddr, 'r') as f:
	geckoData = json.load(f)

geckoKeys = list(geckoData.keys())

geckoDataBtcUsd = geckoData['BtcUsd']





# datetime / epoch variables
today = datetime.datetime.now()
today = str(today).split(".")
today = today[0]
todaySplit = str(today).split(" ")
todayYmd = todaySplit[0]
unixToday = datetimeToUnix(today)



def getCoinDict(coin, baseCurrency, fromTimeStamp, toTimestamp):
	from pycoingecko import CoinGeckoAPI
	cg = CoinGeckoAPI()

	coinApiRez = cg.get_coin_market_chart_range_by_id(id=coin, vs_currency=baseCurrency, from_timestamp=fromTimeStamp, to_timestamp=toTimestamp) # coin gecko coinApiRez
	coinRezPrices = coinApiRez['prices']
	coinRezVolumes = coinApiRez['total_volumes']

	volumeDict, priceDict = {}, {}
	for price in coinRezPrices:
		priceIndex = coinRezPrices.index(price)
		unixTime = price[0]
		volume = coinRezVolumes[priceIndex][1]
		unixTime = int(str(unixTime)[:-3])
		price = price[1]
		localDT = unixToDatetime(unixTime)

		priceDict.update({localDT: price})
		volumeDict.update({localDT: volume})

	returnDict = {"base": baseCurrency, "quote": coin, "data": priceDict, "volumeData": volumeDict}

	return returnDict




def updateGeckoData(currentGeckoDict):
	currentBase = currentGeckoDict['base']
	currentQuote = currentGeckoDict['quote']
	currentGeckoPriceData = currentGeckoDict['data']
	currentGeckoVolumeData = currentGeckoDict['volumeData']

	currentDates = list(currentGeckoPriceData.keys())
	currentDates.sort(reverse=False)
	lastDate = currentDates[-1]
	if lastDate < todayYmd:
		unixLastDate = datetimeToUnix(lastDate)
		updateData = getCoinDict(currentQuote, currentBase, unixLastDate, unixToday)
		updatedPriceData = updateData['data']
		updatedVolumeData = updateData['volumeData']

		currentGeckoPriceData.update(updatedPriceData)
		currentGeckoVolumeData.update(updatedVolumeData)

	else:
		print("Current dictionary is up to date")



updateTest = updateGeckoData(geckoDataBtcUsd)





jsonOutAddr = 'data/gTest' + '.json'
try:
	with open(jsonOutAddr, 'w') as fp1: json.dump(geckoData, fp1)


	print("\nSuccess Creating Crypto Json on/at: " + str(jsonOutAddr) + "\n")

except Exception as e:
	print(e)


