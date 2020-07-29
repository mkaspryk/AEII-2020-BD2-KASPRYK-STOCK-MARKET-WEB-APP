from django import forms
from crypto_guilds.models import Guild

class GuildForm(forms.ModelForm):
    name = forms.CharField(required = True, max_length=50, min_length=5)
    max_members = forms.IntegerField(min_value=1, max_value=50, required = True)
    initial_money = models.DecimalField(max_digits=20,decimal_places=2, required = True)

    class Meta:
        model = Guild
        fields = ('name','max_members','money')
