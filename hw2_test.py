from weather import AirportWeather
import pytest




key = "f8f8eae96c8a82ebcd0b7e784460fe8f"

def testcase():
	assert AirportWeather("vasdfva", key)[0] == 0
	assert AirportWeather("vafdvav", key)[1] == "airportName is wrong."
	assert AirportWeather("Watts Field", 'wrongkey')[0] == 0
	assert AirportWeather("Watts Field", 'wrongkey')[1] == "fail to load weather information"
	assert type(AirportWeather("Watts Field", key)[0]) != int
	assert type(AirportWeather("Watts Field", key)[0]) == type((1,2,3))


