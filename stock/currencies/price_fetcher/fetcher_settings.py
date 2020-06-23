# provider: coingecko.com
# currencies being currently fetched by fetcher.py:
# (to see all possible currencies, visit https://api.coingecko.com/api/v3/coins/list)

from django.conf import settings  # to use django's ORM

settings.configure(
    DATABASE_ENGINE='django.db.backends.mysql',
    DATABASE_NAME='stockmastersdatabase',
    DATABASE_USER='azureuser@stockmastersserver',
    DATABSE_PASSWORD='TW*$Y%sdjfh',
    DATABASE_HOST='stockmastersserver.mysql.database.azure.com',
    DATABASE_PORT=3306
)

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

# interval between fethes per second
interval = 10

# how many records will be stored in a cache file before they are pushed to database all at once
cache_size = 50
