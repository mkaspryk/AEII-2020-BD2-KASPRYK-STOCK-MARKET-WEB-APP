from currencies.models import PriceTimeStamp
from django.http import HttpResponse

def prices(request):
	obj = PriceTimeStamp.objects.last()
	return HttpResponse(obj.to_json())