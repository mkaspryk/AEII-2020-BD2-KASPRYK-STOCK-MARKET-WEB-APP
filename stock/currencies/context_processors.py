from currencies.models import Currency

def extras(request):
    currencies = Currency.objects.all()
    return {'currencies': currencies}

