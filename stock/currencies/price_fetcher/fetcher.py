# this script is used to fetch current cryptocurrencies prices.json every 10 seconds
#  it should run 24/7 because fetched data are stored in the DB to create consistent history of prices.json changes

import requests
import urllib
import json
import os
import time
# noinspection PyUnresolvedReferences,PyPackageRequirements
import fetcher_settings as settings  # ignore the error here if you have one, it should work


def fetch_prices():
    url = settings.base_url + urllib.parse.urlencode(settings.url_parameters)
    currencies_info = {}
    print(url)
    try:
        fetched_data = requests.get(url).json()
        for row in fetched_data:
            currency_symbol = row['symbol']
            current_price = row['current_price']
            currencies_info[currency_symbol] = current_price
    except:
        print("error occurred")
    print(currencies_info)
    return currencies_info


def fetch_prices_loop():
    counter = 0
    while True:
        # with open(os.path.join('.cached_prices', f'prices_{int(time.time())}'), 'w') as f:
        with open(os.path.join('.cached_prices', 'prices.json'), 'w') as f:
            prices = fetch_prices()
            prices_json = json.dumps(prices)
            f.write(prices_json)
            counter = counter+1
            if counter == settings.interval:
                push_cached_prices()
                counter = 0
        time.sleep(settings.interval)


def push_cached_prices():
    print("uploading cached prices.json to DB")


fetch_prices_loop()
