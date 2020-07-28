from django.db import models

class Guild(models.Model):
    guild_name = models.CharField(max_length=50)
    guild_master = models.CharField(max_length=50)
    guild_members = models.TextField()
    guild_score = models.IntegerField()
    guild_money = models.FloatField()

    def __str__():
        return self.guild_name
