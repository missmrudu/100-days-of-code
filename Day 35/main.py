import requests
from twilio.rest import Client
import dotenv

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
weather_api_key = 'd8cfd610dfc8843de37f582d50de6a69'
LATITUDE = 18.520430
LONGITUDE = 73.856743

env = dotenv.dotenv_values()
twilio_api_key = env.get("TWILIO_API_KEY_SID")
twilio_secret = env.get("TWILIO_CLIENT_SECRET")
twilio_account_sid = env.get("TWILIO_ACCOUNT_SID")
twilio_template_sid = "HXac51c61af94371da7904a767b414c2fc"
client = Client(twilio_api_key, twilio_secret, twilio_account_sid)

parameters = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'appid': weather_api_key,
    'cnt': 4,
}

response = requests.get(OWM_Endpoint, params=parameters )
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    message = client.messages.create(
        from_="whatsapp:+17372508034",
        to="whatsapp:+919712944886",
        content_sid=twilio_template_sid
    )
    print(message.body)