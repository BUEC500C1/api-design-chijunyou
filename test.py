from weather import AirportWeather




key = 

def erro_test():
	assert getWeather("xxxxxx", key)[0] == 0
	assert getWeather("xxxxxx", key)[1] == "fail to find the name"
	assert getWeather("Watts Field", 'wrongkey')[0] == 0
	assert getWeather("Watts Field", 'wrongkey')[1] == "fail to load weather information"

def test():
	assert getWeather("Aero B Ranch Airporta", key) == [['2020-02-18 03:00:00', 4, 'Clouds'], ['2020-02-18 06:00:00', 2, 'Clouds'], ['2020-02-18 09:00:00', 1, 'Clouds'], ['2020-02-18 12:00:00', 0, 'Clouds'], ['2020-02-18 15:00:00', 0, 'Clouds'], ['2020-02-18 18:00:00', 5, 'Clouds'], ['2020-02-18 21:00:00', 7, 'Clouds'], ['2020-02-19 00:00:00', 6, 'Clouds'], ['2020-02-19 03:00:00', 3, 'Clouds']]
	