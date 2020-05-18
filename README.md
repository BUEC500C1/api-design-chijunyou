## api design Junyou Chi
# Desciption
With using openweather api and airport data, my api can give a 24-hour weather inforamtion for any airport in the data file.

# install
First run conda "install -r requirements.txt"
Import api by typing "from weather import AirportWather"

# How to use
Use fuction "AirportWeather(Airport, APIKey)" to get weather.
The return from function will be a list.
If the first item is 0, the function is false to get the information. Otherwise, the return is the information. 



        
