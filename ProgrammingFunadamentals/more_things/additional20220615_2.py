# bitcoin price example with API
import requests

# # api key / request url
# key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
#
# # request data from url
# data = requests.get(key)
# data = data.json()
# print(data)
# print(f"{data['symbol']} price is {data['price']}")

# Version 2: get all prices
# api key / request url
key = "https://api.binance.com/api/v3/ticker/price"

# request data from url
data = requests.get(key)
data = data.json()
# print(data)
for x in data:
    print(f"{x['symbol']} price is {x['price']}")