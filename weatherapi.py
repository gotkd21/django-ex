# Get data from Api

import requests



WEATHERSITE = "https://api.darksky.net/"
APICALL = "forecast/"
HOME = "42.19364,-87.96736"
API_KEY = "4c8784bca3dd0691b9b516c8bdea1734"

weather = requests.get(WEATHERSITE + APICALL + API_KEY + "/" + HOME)

print(weather.json())
