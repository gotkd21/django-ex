# Get data from Api

import requests

# Define key Dictionaries
bar_forecast = {}


# Define API Call parameters
WEATHERSITE = "https://api.darksky.net/"
APICALL = "forecast/"
HOME = "42.19364,-87.96736"
API_KEY = "4c8784bca3dd0691b9b516c8bdea1734"
flags = "?exclude=[minutely,alerts,flags]"

# Get current forecast from API and return into json object
cur_forecast = requests.get(WEATHERSITE + APICALL + API_KEY + "/" + HOME + flags)

bar_forecast = cur_forecast.json()

print(bar_forecast)
# Pull location data out of Forecast object
loc_forecast = [bar_forecast['latitude'], bar_forecast['longitude']]
pressure_current = [bar_forecast['currently']['time'],bar_forecast['currently']['pressure']]

print(loc_forecast, " ", pressure_current)


print(type(bar_forecast['hourly']), type(bar_forecast['hourly']['data']))


for fcast in bar_forecast['hourly']['data']:
    print(fcast['time'], " ", fcast['pressure'])
