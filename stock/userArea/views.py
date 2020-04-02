from django.shortcuts import render

# Create your views here.

def userArea(request):
	return render(request, 'userArea.html', {})