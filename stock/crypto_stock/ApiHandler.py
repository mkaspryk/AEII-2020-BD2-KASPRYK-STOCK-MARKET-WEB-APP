import requests
import json
from requests.models import PreparedRequest

class ApiHandler:
    def __init__(self):
        self.api_key = '91f2304795012ff76d8b626a23279468c28a6d8139b9ca07a9e9fcddb323c84d'
        self.coin_list_url = 'https://min-api.cryptocompare.com/data/all/coinlist'
        self.daily_historical_data_url = 'https://min-api.cryptocompare.com/data/v2/histoday'
        self.hourly_historical_data_url = 'https://min-api.cryptocompare.com/data/v2/histohour'
        self.minute_historical_data_url = 'https://min-api.cryptocompare.com/data/v2/histominute'
        self.crypto_symbol_param = 'fsym'
        self.currency_symbol_param = 'tsym'
        self.data_limit_param = 'limit'

    def get_history(self,crypto_symbol,currency_symbol,data_url,data_limit='10') :
        params = { self.crypto_symbol_param : crypto_symbol, self.currency_symbol_param : currency_symbol, self.data_limit_param : data_limit }
        req = PreparedRequest()
        req.prepare_url(data_url,params)
        daily_history_data = requests.get(req.url)
        json_text = json.loads(daily_history_data.content)
        json_data = json_text['Data']['Data']
        return json_data

    def get_daily_history(self,crypto_symbol,currency_symbol,data_limit='10'):
        return self.get_history(crypto_symbol,currency_symbol,self.daily_historical_data_url,data_limit)

    def get_hourly_history(self,crypto_symbol,currency_symbol,data_limit='10'):
        return self.get_history(crypto_symbol,currency_symbol,self.hourly_historical_data_url,data_limit)


    def get_minute_history(self,crypto_symbol,currency_symbol,data_limit='10'):
        return self.get_history(crypto_symbol,currency_symbol,self.minute_historical_data_url,data_limit)
