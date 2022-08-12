from six.moves import urllib
import requests
import pandas as pd
import time

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'x-messari-api-key': '',
        'x-api-realtime-e': '',
    }

information = dict()

def request_data():
    for page in range(1,335):
        url = "https://data.messari.io/api/v1/markets?page=" + str(page)
        data = requests.get(url, headers=headers).json()

        asserts = data['data']
        for i in asserts:
            exchange = i['exchange_name']
            coin = i['base_asset_symbol']
            if coin not in information:
                information[coin] = [exchange]
            else:
                information[coin].append(exchange)

try:
    request_data()
except:
    time.sleep(20)
    try:
        request_data()
    except:
        time.sleep(20)
        try:
            request_data()
        except:
            time.sleep(20)


market_data = pd.DataFrame({'coin': list(information.keys()), 'exchange': list(information.values())})
market_data.to_csv("market_data.csv")
