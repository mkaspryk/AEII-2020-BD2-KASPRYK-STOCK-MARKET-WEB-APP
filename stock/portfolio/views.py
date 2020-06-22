from django.shortcuts import render

# Create your views here.

def portfolio(request):
	return render(request, 'portfolio.html', context={"growValue": 54})

def welcome(request):
	return render(request, 'welcome.html', {})

