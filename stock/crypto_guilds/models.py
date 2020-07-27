from django.db import models

class Guild(models.Model):
    guild_name = models.CharField(max_length=50)
    guild_members = models.TextField(null=True)
    guild_score = models.IntegerField()
    guild_money = models.FloatField()
