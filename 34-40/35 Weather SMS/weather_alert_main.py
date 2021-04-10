import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

MY_LAT = 37.1243
MY_LONG = -77.2264
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "52b85f4447b54dc9586a50465d83d0e1"
account_sid = "AC9b290ef413b50fac2a355b47cdd26d47"
auth_token = "908fe514a7967894951be6985067bb29"

parameters={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "units": "imperial",
    "exclude": "current,minutely,daily",
    "appid": api_key,

}


response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_slice= weather_data['hourly'][:13]
#[:13] is the slice method.  the : is saying keep everything before this
#a[start:stop:step]
#hourly_data = weather_data["hourly"][0]["weather"][0]["id"]
# first we had say the key is hourly then we said index 0 is weather then index 0 is id

will_rain = False

for hour_data in weather_slice:
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token,http_client=proxy_client)

    message = client.messages \
        .create(
        body="Dude you got this!! Make that cheddar baby!.",
        from_="+12562902565",
        to="18035421156",
    )
    print(message.status)



# api_key = "52b85f4447b54dc9586a50465d83d0e1"
#
#
# api_call ="api.openweathermap.org/data/2.5/weather?q=Richmond,us&appid="
#
# api= api_call + api_key
#
# print(api)
#
# response= requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=37.1243&lon=-77.2264&units=imperial&appid=52b85f4447b54dc9586a50465d83d0e1")
# response.raise_for_status()
# data = response.json()
#
# print(data)