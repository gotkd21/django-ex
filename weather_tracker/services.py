# Get data from Api

import requests
import time

def get_weatherdata(location,time_req):

    # Define key Dictionaries
    bar_forecast = {}
    location = ""
    cur_time = int(time.time())
    time_req = ""

    # Define API Call parameters
    WEATHERSITE = "https://api.darksky.net/"
    default_location = "42.19364,-87.96736"
    API_KEY = "4c8784bca3dd0691b9b516c8bdea1734"
    FLAGS = "?exclude=[minutely,alerts,flags]"
    API_CALL = "forecast/"

    #set active_location
    if len(location) < 2:
        active_location = default_location
    else:
        active_location = location

    if len(time_req) < 5:
        active_location_time = active_location + "," + str(cur_time)
    else:
        active_location_time = active_location + "," + str(time_req)
    # Get current forecast from API and return into json object
    cur_forecast = requests.get(WEATHERSITE + API_CALL + API_KEY + "/" + active_location_time + FLAGS)
    bar_forecast = cur_forecast.json()

    # Pull location data out of Forecast object
    #loc_forecast = [bar_forecast['latitude'], bar_forecast['longitude']]
    #pressure_current = [bar_forecast['currently']['time'],bar_forecast['currently']['pressure']]

    #hourly_pressure = {}
    #hourly_pressure = [bar_forecast['hourly']['data']]
    #print(type(hourly_pressure), type(hourly_pressure[0]))

    #print(hourly_pressure)



    #for fcast in bar_forecast['hourly']['data']:
    #    print(fcast['time'], " ", fcast['pressure'])
    return bar_forecast['hourly']['data']
