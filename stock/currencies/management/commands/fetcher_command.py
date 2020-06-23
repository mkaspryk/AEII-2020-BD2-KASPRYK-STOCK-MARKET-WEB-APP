# this script is used to fetch current cryptocurrencies prices.json every 10 seconds
#  it should run 24/7 because fetched data are stored in the DB to create consistent history of prices.json changes

# provider: coingecko.com
# currencies being currently fetched by fetcher_command.py:
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

    def handle(self, *args, **kwargs):
        url = base_url + urllib.parse.urlencode(url_parameters)
        currencies_info = {}
        try:
            fetched_data = requests.get(url).json()
            for row in fetched_data:
                currencies_info[row['symbol'].lower()] = row['current_price']
        except:
            self.stdout.write("error occurred")
        prices = json.dumps(currencies_info)
        self.stdout.write(prices)
        PriceTimeStamp(
            btc_price=currencies_info['btc'],
            eth_price=currencies_info['eth'],
            xrp_price=currencies_info['xrp'],
            ltc_price=currencies_info['ltc'],
            usdt_price=currencies_info['usdt'],
            libra_price=0.00,  # currencies_info['libra'],
            xmr_price=currencies_info['xmr'],
            eos_price=currencies_info['eos'],
            bnb_price=currencies_info['bnb'],
        ).save()
