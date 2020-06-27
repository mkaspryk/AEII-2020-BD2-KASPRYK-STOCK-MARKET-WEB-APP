from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .forms import QuickBuyForm

CHOICES = (('1', "btc"), ('2', "eth"))

def perform_quick_buy(request):
    if request.method == 'POST' and request.user.is_authenticated:
        buy_amount = request.POST.get('buy_amount')
        buy_currency = request.POST.get('buy_currency')
        pay_amount = request.POST.get('pay_amount')
        pay_currency = request.POST.get('pay_currency')
        print(f"buying {buy_amount} {buy_currency} for {pay_amount} {pay_currency}...")
    return HttpResponse('')
