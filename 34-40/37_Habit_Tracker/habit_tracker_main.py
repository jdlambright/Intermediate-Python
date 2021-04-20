import requests
from datetime import datetime

USERNAME = "lambo4"
TOKEN = "ajksfdkbasvoas"
GRAPH_ID= "graph2"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)
#we do response.text because instead of giving 200 it will say something like user name exist

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Hours Studying Graph",
    "unit": "hrs",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN":TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

today = datetime(year=2021, month=4, day=20)
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5.5"}

response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
print(response.text)

#update a pixel
update_delete_endpoint = f"{pixel_creation_endpoint}/20210411"
#
# update_params = {
#     "quantity": "6"
# }
#
# response = requests.put(url=update_delete_endpoint, json=update_params, headers=headers)
# print(response.text)

#delete a pixel
# response = requests.delete(url=update_delete_endpoint, headers=headers)
# print(response.text)





