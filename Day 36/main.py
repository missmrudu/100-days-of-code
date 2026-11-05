import requests
import dotenv

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

env = dotenv.dotenv_values()
stock_api_key =  env.get("STOCK_API_KEY")
news_api_key = env.get("NEWS_API_KEY")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apiKey":stock_api_key,
}
response = requests.get(STOCK_ENDPOINT,params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
daya_before_closing_price = day_before_yesterday_data["4. close"]
print(daya_before_closing_price)

difference = abs(float(yesterday_closing_price) - float(daya_before_closing_price))
print(difference)

diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)


if diff_percent > 1:
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

    three_articles = articles[:3]
    print(three_articles)

