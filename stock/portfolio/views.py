from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from funds.models import Fund
from decimal import Decimal


def calculate_balance(funds):
	sumofnums = Decimal(0)
	for fund in funds:
		sumofnums = sumofnums + fund.get_dollar_value()
	return sumofnums


def portfolio(request):
	if request.user.is_authenticated:
		wallet = request.user.userwallet
		funds = wallet.fund_set.all()
		return render(request, 'portfolio/portfolio.html', context={"balance": calculate_balance(funds), "funds": funds})
	else:
		return HttpResponseNotFound("wyjazd stad kurw a")
