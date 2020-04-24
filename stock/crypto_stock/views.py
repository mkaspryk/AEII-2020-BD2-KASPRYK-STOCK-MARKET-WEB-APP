from django.shortcuts import render
from . import api_handling
from . import graphs


def crypto_stock(request):
    if request.method == 'POST':
        graphs.return_app(request.POST['crypto_search'])
    else:
        graphs.return_app('BTC')
    api_handler = api_handling.ApiHandler()
    daily_history_data = api_handler.get_daily_history('BTC', 'USD')
    return render(request, 'crypto_stock.html', {'daily_history_data': daily_history_data})
