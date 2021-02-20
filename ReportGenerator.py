# -*- coding: utf-8 -*-
"""
Weather API
Created on Sat Feb 20 12:23:30 2021

@author: yubin
"""

import requests
url = "https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={APIkey}"
url = url.format(cityName='Berkeley',APIkey="f48c1eff081887675a7918bb9550df2e")
x = requests.get(url)
print(x.status_code)
print(x)