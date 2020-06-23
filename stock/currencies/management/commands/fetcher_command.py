# this script is used to fetch current cryptocurrencies prices.json every 10 seconds
#  it should run 24/7 because fetched data are stored in the DB to create consistent history of prices.json changes

# provider: coingecko.com
# currencies being currently fetched by fetcher.py:
# (to see all possible currencies, visit https://api.coingecko.com/api/v3/coins/list)

import requests
import urllib
import json
from django.core.management.base import BaseCommand, CommandError
from currencies.models import PriceTimeStamp

base_url = "https://api.coingecko.com/api/v3/coins/markets?"

provider_currencies_ids = [
    'bitcoin',          # 'btc'
    'ethereum',         # 'eth'
    'ripple',           # 'xrp'
    'litecoin',         # 'ltc'
    'tether',           # 'usdt'
    'libra',            # 'libra'
    'monero',           # 'xmr'
    'eos',              # 'eos'
    'binancecoin',      # 'bnb'
]
currency_list = ','.join([currency for currency in provider_currencies_ids])

url_parameters = {
    'ids': currency_list,
    'vs_currency': 'usd',
    'per_page': 100,
    'page': 1,
    'sparkline': 'false',
}

class Command(BaseCommand):
        help = 'Fetches current crypto prices to local database.'

    def handle(self):
        url = base_url + urllib.parse.urlencode(url_parameters)
        currencies_info = {}
        try:
            fetched_data = requests.get(url).json()
            for row in fetched_data:
                currency_symbol = row['symbol']
                current_price = row['current_price']
                currencies_info[currency_symbol] = current_price
        except:
            print("error occurred")
        prices = json.dumps(currencies_info)
        try:
            PriceTimeStamp(
                btc_price=prices['btc'],
                eth_price=prices['eth'],
                xrp_price=prices['xrp'],
                ltc_price=prices['ltc'],
                usdt_price=prices['usdt'],
                libra_price=prices['libra'],
                xmr_price=prices['monero'],
                eos_price=prices['eos'],
                bnb_price=prices['binancecoin'],
            ).save()
        except:
            print("error occured 2")
        return currencies_info
