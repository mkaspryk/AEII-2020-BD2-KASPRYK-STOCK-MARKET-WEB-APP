from django.shortcuts import render

# Create your views here.

def portfolio(request):
	return render(request, 'portfolio.html', {})


def welcome(request):
	return render(request, 'welcome.html', {})

def profile(request):
    return render(request, 'profile.html',{})

def clan(request):
    return render(request, 'clan.html',{})

def stock(request):
    return render(request, 'stocks.html',{})
