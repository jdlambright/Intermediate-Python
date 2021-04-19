import requests

response = requests.get(url="https://api.sheety.co/be411e8cf62d3966a9666c5b539f30ea/flightDeals/sheet1")
response.raise_for_status()
data = response.text
print(data)




class FlightData:
    #This class is responsible for structuring the flight data.
    pass