from django import forms

class GuildForm(forms.Form):
    guild_name = forms.CharField(required = True)
    max_members = forms.IntegerField(required = True)
    initial_money = forms.FloatField(required = True)
