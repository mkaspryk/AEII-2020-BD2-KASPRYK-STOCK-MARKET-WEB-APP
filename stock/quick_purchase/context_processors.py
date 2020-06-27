from quick_purchase.forms import QuickBuyForm

def quick_buy_form_context(request):
    if request.user.is_authenticated:
        fund_set = request.user.userwallet.fund_set.all()
        pay_choices = []
        for index, fund in enumerate(fund_set):
            pay_choices.append((fund.currency.symbol, str(index)))
    else:
        pay_choices = [('chujstwo', '1')]
    print(pay_choices)
    return {'quick_buy_form': QuickBuyForm()}

def available_currencies_context(request):
    if request.user.is_authenticated:
        fund_set = request.user.userwallet.fund_set.all()
        currencies = []
        for fund in fund_set:
            currencies.append(fund.currency.symbol)
            print(fund.currency.symbol)
        return {'available_currency_set': currencies}
    return {}
