from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import QuickBuyForm

def buy(request):
    if request.method == 'POST':
        form = QuickBuyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # correctly prints buy/pay data
            return HttpResponseRedirect('/')
    else:
        form = QuickBuyForm()
    return render(request, 'quick_purchase/quick_buy.html', {'form': form})
