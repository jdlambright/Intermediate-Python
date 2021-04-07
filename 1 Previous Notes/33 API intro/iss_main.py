import requests
from datetime import datetime

MY_LAT = 37.1243
MY_LONG = 77.2264

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# quote = response.json()
#
# longitude = quote["iss_position"]["longitude"]
# latitude = quote["iss_position"]["latitude"]
#
# lat_long_tuple = (longitude, latitude)
#
# print(quote)

parameters ={
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data= response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])

# time_now = datetime.now()
# print(time_now)














'''
line 1 
    request is the library used for api's

line 5:
    different response codes and what they mean
    100's: hold on
    200's: here you go
    300's: go away
    400's: you screwed up
    500's: the server screwed up
    
    response has lots of built in code to automatically raise a status code no matter what it is
    
line 6: 
    to get the actual data instead of a status code we have to use the .json method
    everything in the [] is drilling down specifically what we want

'''