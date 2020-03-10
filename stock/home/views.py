
from django.shortcuts import render

def index(request):
	return render(request, 'index.html', {})

def register(request):
	return render(request, 'registerPanel.html',{})

def login(request):
	return render(request, 'loginPanel.html',{})

