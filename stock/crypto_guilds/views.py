from django.shortcuts import render
from crypto_guilds.models import Guild
from crypto_guilds.forms import JoinGuildForm
from django.template import RequestContext

def crypto_guilds(request):

	if request.method == 'GET':
		form = JoinGuildForm()
		return render(request, 'crypto_guilds/crypto_guilds.html',{'guilds': Guild.objects.all(), 'form': form})
	elif request.method == 'POST':
		request.user.guildmember.guild = Guild.objects.filter(guild_name = request.POST.get("guild_name",""))[0]
		request.user.save()
		return render(request, 'crypto_guilds/crypto_guilds.html',{'guilds': Guild.objects.all()})
