from quick_purchase.forms import QuickBuyForm

def extras(request):
    quick_buy_form = QuickBuyForm()
    return {'quick_buy_form': quick_buy_form}

