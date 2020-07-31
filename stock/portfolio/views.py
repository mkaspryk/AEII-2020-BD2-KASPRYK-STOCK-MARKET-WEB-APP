from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from funds.models import Fund
from decimal import Decimal

from currencies.models import Currency


def portfolio(request):
	if request.user.is_authenticated:
		wallet = request.user.userwallet
		funds = wallet.fund_set.all()
		guild = request.user.guildmember.guild
		return render(request, 'portfolio/portfolio.html', context={"balance": wallet.calculate_balance(), "funds": funds, 'guild': guild})
	else:
		return HttpResponseNotFound("wyjazd stad kurw a")

def perform_sell(request, currId):
    currency = Currency.objects.get(id=currId)

    user_funds = request.user.userwallet.fund_set.all()
    user_current_fund = None

    for fnd in user_funds:
        if fnd.currency.id == currId:
            user_current_fund = fnd
            break

    print(user_current_fund.amount)
    request.user.userwallet.perform_sell_transaction(user_current_fund.amount,currency)

    print(f"selled {currId} {currency.name}")
    return portfolio(request)
