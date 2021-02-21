# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 00:41:12 2021

@author: yubin
"""

template="""Hi Ms. Fan, how are you doing today madam? The weather in the city of {city} today is going to be mostly {weather}. The high temperature is going to be {temp_max} and the low temperature is going to be {temp_min}. The wind is mostly going to be from the {direction} direction. The speed of the wind is going to be around {wind_speed}. The visibility should be around {visibility}. While the sun rise is expected at {sun_rise}, the sunset is going to be at {sun_set}. Additional information on the position of astronomical bodies in the solar system can be found at https://ssd.jpl.nasa.gov/horizons.cgi
The high tides in Berkeley Marina is going to be at {high_tide1} and {high_tide2}. The low tides are going to be around {low_tide1}. 
"""
city = "Berkeley"
weather = "sunny"
temp_max = "17 degrees Celsius"
temp_min = "7 degrees Celsius"
direction = "North"
wind_speed = "2m/s"
visibility = "12.9km"
sun_rise = "6:50am"
sun_set = "5:54pm"
high_tide1 = "6:26am"
high_tide2 = "9:11pm"
low_tide1 = "2:00pm"



result = template.format(city=city, weather=weather, temp_max=temp_max,temp_min=temp_min,
                         direction=direction,wind_speed=wind_speed,visibility=visibility,
                         sun_rise=sun_rise,sun_set=sun_set,high_tide1=high_tide1,
                         high_tide2=high_tide2,low_tide1=low_tide1)

print(result)