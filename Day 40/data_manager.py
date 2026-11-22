import requests
import dotenv
from requests.auth import HTTPBasicAuth

env = dotenv.dotenv_values()
USER_ID = env.get("USER")
PASSWORD = env.get("PASS")
sheety_url = 'https://api.sheety.co/ca9747eb2e9a2bc6f1978f63585120ba/flightDeals/prices'


class DataManager:
    def __init__(self):
        self.user_id = USER_ID
        self.password = PASSWORD
        self.authorization = HTTPBasicAuth(self.user_id, self.password)

    def destination_data(self):
        response = requests.get(url=sheety_url,auth=self.authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{sheety_url}/{row_id}",
            json=new_data,
            auth=self.authorization
        )