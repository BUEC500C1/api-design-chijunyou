from weather import AirportWeather




key = "f8f8eae96c8a82ebcd0b7e784460fe8f"

def erro_test():
	assert AirportWeather("vasdfva", key)[0] == 0
	assert AirportWeather("vafdvav", key)[1] == "fail to find the name"
	assert AirportWeather("Watts Field", 'wrongkey')[0] == 0
	assert AirportWeather("Watts Field", 'wrongkey')[1] == "fail to load weather information"
