from django.shortcuts import render
from . import api_handling, plotting
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from . import graphs


def crypto_stock(request):
	if request.method == 'POST':
		graphs.return_app(request.POST['crypto_search'])
	else:
		graphs.return_app('BTC')
	api_handler = api_handling.ApiHandler()
	daily_history_data = api_handler.get_daily_history('BTC','USD')
	fig = plotting.prepare_graf(daily_history_data, 'Bitcoin Chart', 'lines+markers')
	return render(request, 'crypto_stock.html', {'daily_history_data': daily_history_data})
