
from django.shortcuts import render

# Create your views here.

def adminArea(request):
	return render(request, 'adminArea.html', {})


