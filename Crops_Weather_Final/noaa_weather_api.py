from ast import Return
from time import sleep
from turtle import color
import requests
import pandas as pd
import geocoder

def weather_data_pandas_frame():
    geo = geocoder.ip('me')
    gll = geo.latlng
    lat = str(gll[0])
    lon = str(gll[1])
    latlon = lat + "," + lon
   
### Retrieve forecast API URLs for grid location from NOAA
    noaa_find_grid_URL = "https://api.weather.gov/points/" + latlon

    noaapoints = requests.get(noaa_find_grid_URL)

    noaapoints_json = noaapoints.json()
    noaa_forecast_URL = noaapoints_json['properties']['forecast']
    noaa_hourly_URL = noaapoints_json['properties']['forecastHourly']
    noaa_forecast_grid_URL = noaapoints_json['properties']['forecastGridData']

### Set Variables for JSON data return
    weatherforecast = requests.get(noaa_forecast_URL)
    hourlyforecast = requests.get(noaa_hourly_URL)
    forecastgrid = requests.get(noaa_forecast_grid_URL)
    weatherforecast_json = weatherforecast.json()
    hourlyforecast_json = hourlyforecast.json()
    forecastgrid_json = forecastgrid.json()

### Create dataframe with formatted results for display
    df_weather_init = pd.DataFrame(hourlyforecast_json['properties']['periods'])
    df_weather_init['startTime_substring'] = df_weather_init.startTime.str.slice(11, 16)
    df_weather_second= df_weather_init[['startTime_substring','temperature', 'shortForecast']]
    df_weather_second.columns.values[0] = "Time"
    df_weather_second.columns.values[1] = "Temperature"
    df_weather_second.columns.values[2] = "Forecast"
    df_weather_final = df_weather_second.iloc[0:4, 0:3]
###print(df_weather_final.iloc[0:4, 0:3])
    return df_weather_final

def get_noaa_weather():
    try: 
        weather_data_pandas_frame()
        return weather_data_pandas_frame()
    except: 
        sleep(3)
        return weather_data_pandas_frame()
    finally:
        return weather_data_pandas_frame()