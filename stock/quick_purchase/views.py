from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from decimal import Decimal
from .forms import QuickBuyForm
from currencies.models import Currency

def perform_quick_buy(request):
    if request.method == 'POST' and request.user.is_authenticated:
        buy_amount_str = request.POST.get('buy_amount')
        buy_currency_str = request.POST.get('buy_currency')
        pay_currency_str = request.POST.get('pay_currency')
        buy_amount = Decimal(buy_amount_str)
        buy_currency = Currency.objects.get(id=buy_currency_str)
        pay_currency = Currency.objects.get(id=pay_currency_str)
        pay_amount = buy_currency.convert_amount_to(buy_amount, pay_currency)
        print("price:", pay_amount, pay_currency.id)
        if request.user.userwallet.is_solvent(pay_amount, pay_currency):
            print("wyplacalny")
            request.user.userwallet.perform_transaction(pay_amount, pay_currency, buy_amount, buy_currency)
        else:
            print("niewyplacalny")
        # TODO transaction

    return HttpResponse('')
