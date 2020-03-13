from django.shortcuts import render
from . import ApiHandler


def crypto_stock(request):
	api_handler = ApiHandler.ApiHandler()
	api_handler.get_daily_history('BTC','USD')
	return render(request, 'crypto_stock.html', {})
