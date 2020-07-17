# this script is used to fetch current cryptocurrencies prices.json every 10 seconds
#  it should run 24/7 because fetched data are stored in the DB to create consistent history of prices.json changes

# provider: coingecko.com
# currencies being currently fetched by fetcher_command.py:
# (to see all possible currencies, visit https://api.coingecko.com/api/v3/coins/list)

import requests
import urllib
import json
from django.core.management.base import BaseCommand, CommandError
from currencies.models import Currency
from currencies.app_settings import currencies

base_url = "https://api.coingecko.com/api/v3/coins/markets?"

currency_list = ','.join([currency for currency in currencies])

url_parameters = {
    'ids': currency_list,
    'vs_currency': 'usd',
    'per_page': 100,
    'page': 1,
    'sparkline': 'false',
}


# Fetches current crypto prices to local database.
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = base_url + urllib.parse.urlencode(url_parameters)
        self.stdout.write("Fetching from:\n" + url)
        fetched_data = requests.get(url).json()
        price_timestamp = {}
        for row in fetched_data:
            curr = None
            if Currency.objects.filter(name=row['id']).exists():
                curr = Currency.objects.get(name=row['id'])
                curr.symbol = row['symbol']
                curr.current_price = row['current_price']
                curr.market_cap = row['market_cap']
                curr.total_volume = row['total_volume']
                curr.high_24h = row['high_24h']
                curr.low_24h = row['low_24h']
                curr.price_change_24h = row['price_change_24h']
                curr.price_change_percentage_24h = row['price_change_percentage_24h']
            else:  # creates new record
                curr = Currency(
                    name=row['id'],
                    symbol=row['symbol'],
                    current_price=row['current_price'],
                    market_cap=row['market_cap'],
                    total_volume=row['total_volume'],
                    high_24h=row['high_24h'],
                    low_24h=row['low_24h'],
                    price_change_24h=row['price_change_24h'],
                    price_change_percentage_24h=row['price_change_percentage_24h']
                )
            curr.save()
            price_timestamp[curr.name] = curr.current_price
        prices = json.dumps(price_timestamp)
        self.stdout.write(prices)
        # PriceTimeStamp(
        #     bitcoin_price=price_timestamp['bitcoin'],
        #     ethereum_price=price_timestamp['ethereum'],
        #     ripple_price=price_timestamp['ripple'],
        #     litecoin_price=price_timestamp['litecoin'],
        #     tether_price=price_timestamp['tether'],
        #     tezos_price=price_timestamp['tezos'],
        #     monero_price=price_timestamp['monero'],
        #     eos_price=price_timestamp['eos'],
        #     binancecoin_price=price_timestamp['binancecoin'],
        # ).save()

