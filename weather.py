import sys
import csv
import requests


def AirportWeather(Airport, APIKey):
	rtn = list()
	findname = False
	try:
		with open('./data.csv', 'r') as f:
			reader = csv.reader(f)
			for row in reader:
				if  Airport == row[3]:
					lat = str(int(float(row[4])))
					lon = str(int(float(row[5])))
					findname = True
					break
	except:
		rtn.append(0)
		rtn.append("fail to find the name")
		return rtn

	if not findname:
		rtn.append(0)
		rtn.append("airportName is wrong.")
		return rtn


	try:
		link = "https://api.openweathermap.org/data/2.5/forecast?lat=" + lat + "&lon=" + lon + "&appid=" + APIKey
		jsonfile = requests.get(link).json()
	except:
		rtn.append(0)
		rtn.append("fail to load weather information")
		return rtn

	
	for i in range (0,9):
		weatherinformation = list()
		time = jsonfile['list'][i]["dt_txt"]
		temperature = int(float(jsonfile['list'][i]['main']['temp']) - 273)
		weather = jsonfile['list'][i]['weather'][0]['main']
		weatherinformation.append(time)
		weatherinformation.append(temperature)
		weatherinformation.append(weather)
		rtn.append(weatherinformation)



	return rtn

def main():

	airportName = "Aero B Ranch Airporta"
	APIKey = "f8f8eae96c8a82ebcd0b7e784460fe8f"
	rtn = AirportWeather(airportName, APIKey)
	print(rtn)

if __name__=="__main__":
  main()