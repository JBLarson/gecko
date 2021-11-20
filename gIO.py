
import json

def createJsonFunc(jsonOutAddr, jsonData):
	try:
		with open(jsonOutAddr, 'w') as fp1: json.dump(jsonData, fp1)
		functionOutput = ("\nSuccess Creating JSON at: " + str(jsonOutAddr) + "\n")

	except Exception as e:
		functionOutput = "\nFailed to create JSON. Error msg:\n" + str(e)

	return functionOutput




def readJsonFunc(jsonInAddr):
	with open(jsonInAddr, 'r') as r:
		jsonOutputDict = json.load(r)
	return jsonOutputDict

