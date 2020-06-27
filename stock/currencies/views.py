from currencies.models import Currency
from django.http import HttpResponseNotFound, JsonResponse

def prices(request):
	if request.is_ajax():
		currencies = list(Currency.objects.all().values('id', 'current_price', 'price_change_percentage_24h'))
		return JsonResponse(currencies, safe=False)
	return HttpResponseNotFound()



