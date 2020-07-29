from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class GuildMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    guild = models.ForeignKey('crypto_guilds.Guild', on_delete=models.SET_NULL, default=None, null=True)

class Guild(models.Model):
    guild_name = models.CharField(max_length=50, blank = False)
    master = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    max_members = models.IntegerField(blank = False, validators=[MaxValueValidator(50),MinValueValidator(1)])
    score = models.IntegerField()
    money = models.DecimalField(max_digits=20,decimal_places=2, blank = False)
