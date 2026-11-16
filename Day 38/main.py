import requests
import dotenv
from datetime import datetime

GENDER = "female"
HEIGHT = 155
WEIGHT = 53
AGE = 18

env = dotenv.dotenv_values()
ID = env.get("APP_ID")
KEY = env.get("API_KEY")

nutrition_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_test = input("Enter the exercises you did:")

headers = {
    "x-app-id": ID,
    "x-app-key": KEY,
}

params = {
    "query": exercise_test,
    "gender": GENDER,
    "height": HEIGHT,
    "weight": WEIGHT,
    "age": AGE,
}

response = requests.post(url = nutrition_endpoint, json = params, headers = headers)
result = response.json()
print(result)
