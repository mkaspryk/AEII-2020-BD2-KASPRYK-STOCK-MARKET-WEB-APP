from django.shortcuts import render
from . import ApiHandler
import json


def crypto_stock(request):
	api_handler = ApiHandler.ApiHandler()
	daily_history_data = api_handler.get_daily_history('BTC','USD')
	return render(request, 'crypto_stock.html', {'daily_history_data': daily_history_data})
