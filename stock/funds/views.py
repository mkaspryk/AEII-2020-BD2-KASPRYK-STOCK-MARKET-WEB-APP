from django.shortcuts import render
from funds.models import StockFund
from funds.models import StockFundUser
from currencies.models import Currency
from portfolio.models import UserWallet
from django.contrib.auth.models import User
# Create your views here.

def stockfund(request):
	return render(request, 'stockfund.html')
	
	
def create_fund(request):
	if request.method == "POST":
		postUsername = request.POST.get('userName')
		fundname = request.POST.get('fundName')
		try:
			detectedUser = User.objects.get(username = postUsername)
		except User.DoesNotExist:
			detectedUser = User(username = postUsername)
			detectedUser.save()
		newFund = StockFund(name = fundname, amount = 200, currency=Currency.objects.get(name="bitcoin"))
		try:
			newUser = StockFundUser(stockfundname = newFund, isOwner = True, name = postUsername, wallet = UserWallet.objects.get(user = detectedUser))
		except UserWallet.DoesNotExist:
			tmpWallet = UserWallet(amount = 0.0)
			tmpWallet.save()
			newUser = StockFundUser(stockfundname = newFund, isOwner = True, name = postUsername, wallet = tmpWallet)
		newFund.save()
		newUser.save()
		newUser.add_wallet_value(-0.2)
		return render(request, 'stockfund.html',{"StockFund": newFund, "user": newUser})
	else:
		return render(request, 'stockfund.html')
		
def view_fund(request):
	if request.method == "POST":
		relevantFund = StockFund.objects.get(name = request.POST.get('fundName'))
		return render(request, 'stockfund.html',{"StockFund": relevantFund, "user": newUser})
	else:
		return render(request, 'stockfund.html')
		
def join_fund(request):
	if request.method == "POST":
		username = request.POST.get('userName')
		fundname = request.POST.get('fundName')
		try:
			relevantFund = StockFund.objects.get(name = fundname)
		except StockFund.DoesNotExist:
			return render(request, 'stockfund.html')
		try:
			newUser = StockFundUser(stockfundname = relevantFund, isOwner = False, name = username, wallet = UserWallet.objects.get(username))
		except UserWallet.DoesNotExist:
			tmpWallet = UserWallet(amount = 0.0)
			tmpWallet.save()
			newUser = StockFundUser(stockfundname = newFund, isOwner = True, name = postUsername, wallet = tmpWallet)
		newUser.save()
		newUser.add_wallet_value(-0.1)
		return render(request, 'stockfund.html',{"StockFund": relevantFund, "user": newUser})
	else:
		return render(request, 'stockfund.html')
		
	
