from django.shortcuts import render
from crypto_guilds.models import Guild
from guild_creation.forms import GuildForm

def guild_creation(request):

    template_name = 'guild_creation/guild_creation.html'


    if request.method == 'GET':
        form = GuildForm()
        return render(request, template_name, {'form': form})

    if request.method == 'POST':
        form = GuildForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name, {'form': form, 'text': text})
