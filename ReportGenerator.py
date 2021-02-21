# -*- coding: utf-8 -*-
"""
Weather API
Created on Sat Feb 20 12:23:30 2021

@author: yubin
"""

import requests
url = "https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={APIkey}"
forcast = "https://https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"
url = forcast.format(cityName='Berkeley',APIkey="f48c1eff081887675a7918bb9550df2e")
x = requests.get(url)
print(x.status_code)
print(x)

Report = """
Hi Ms. Fan, how are you doing today madam? The weather in the city of {city} today is going to be mostly {weather}. The high temperature is going to be {highTemp} degrees
"""