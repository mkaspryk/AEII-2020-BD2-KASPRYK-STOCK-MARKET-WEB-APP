from django.shortcuts import render

def crypto_guilds(request):
	return render(request, 'crypto_guilds/crypto_guilds.html')
