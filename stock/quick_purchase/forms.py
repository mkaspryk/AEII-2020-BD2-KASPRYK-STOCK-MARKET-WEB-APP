from django import forms

class QuickBuyForm(forms.Form):
    buy_amount = forms.CharField(label='buy_amount', max_length=30)
    pay_amount = forms.CharField(label='pay_amount', max_length=30)