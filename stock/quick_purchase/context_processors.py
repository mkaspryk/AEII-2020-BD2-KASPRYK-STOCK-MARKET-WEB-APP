from quick_purchase.forms import QuickBuyForm

def quick_buy_form_context(request):
    return {'quick_buy_form': QuickBuyForm()}

def available_currencies_context(request):
    if request.user.is_authenticated:
        fund_set = request.user.userwallet.fund_set.all()
        currencies = []
        for fund in fund_set:
            currencies.append(fund.currency)
        return {'available_currency_set': currencies}
    return {}
