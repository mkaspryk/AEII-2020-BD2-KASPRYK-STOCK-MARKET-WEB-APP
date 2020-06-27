from django import forms

CHOICES = (('1', "btc"), ('2', "eth"))

class QuickBuyForm(forms.Form):
    buy_amount = forms.CharField(max_length=30)
    buy_currency = forms.ChoiceField(choices=CHOICES)
    pay_amount = forms.CharField(max_length=30)
    pay_currency = forms.ChoiceField(choices=CHOICES)
