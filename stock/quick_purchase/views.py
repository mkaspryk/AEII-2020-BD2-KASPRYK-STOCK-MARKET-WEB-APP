from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .forms import QuickBuyForm

CHOICES = (('1', "btc"), ('2', "eth"))

def quick_buy(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = QuickBuyForm(request.POST)
            print(form)
            if form.is_valid():
                print(form.cleaned_data)  # correctly prints buy/pay data
                return HttpResponseRedirect('/register/')
    return HttpResponseRedirect('/login/')

def perform_quick_buy(request):
    if request.method == 'POST' and request.user.is_authenticated:
        print(request)
        buy_amount = request.POST.get('buy_amount')
        buy_currency = request.POST.get('buy_currency')
        pay_amount = request.POST.get('pay_amount')
        pay_currency = request.POST.get('pay_currency')
        print(f"buying {buy_amount} {buy_currency} for {pay_amount} {pay_currency}...")
    return HttpResponse('')

