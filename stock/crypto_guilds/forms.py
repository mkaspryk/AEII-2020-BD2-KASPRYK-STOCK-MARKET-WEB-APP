from django import forms
from crypto_guilds.models import Guild

class JoinGuildForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.HiddenInput())
