from currencies.models import Currency, PriceTimeStamp

def extras(request):
    currencies = Currency.objects.all()
    return {'currencies': currencies}

