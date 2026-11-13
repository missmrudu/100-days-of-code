import requests
import dotenv
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

env = dotenv.dotenv_values()
token = env.get("TOKEN")
user = env.get("USER")
graph_id = "graph1"

user_params = {
    "token": token,
    "username": user,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

graph_endpoint = f"{pixela_endpoint}/{user}/graphs"

graph_config = {
    "id":graph_id,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN":token,
}

today = datetime.now()
pixel_creation_endpoint = f"{pixela_endpoint}/{user}/graphs/{graph_id}"
pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity": "20",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)