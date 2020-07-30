from django.shortcuts import render
from crypto_guilds.models import Guild
from crypto_guilds.forms import JoinGuildForm

def crypto_guilds(request):

	if request.method == 'GET':
		form = JoinGuildForm()
		return render(request, 'crypto_guilds/crypto_guilds.html',{'guilds': Guild.objects.all(), 'form': form})
	elif request.method == 'POST':
		form = JoinGuildForm(request.POST)
		if form.is_valid():
			request.user.guildmember.guild = Guild.objects.filter(guild_name = form.name)
			request.user.save()
		return render(request, 'crypto_guilds/crypto_guilds.html',{'guilds': Guild.objects.all()})
