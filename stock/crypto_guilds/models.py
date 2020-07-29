from django.db import models
from django.contrib.auth.models import User

class Guild(models.Model):
    name = models.CharField(max_length=50, required = True)
    master = models.OneToOneField(GuildMember)
    members = model.ForeignKey(GuildMember)
    max_members = models.IntegerField(min_value=1, max_value=50, required = True)
    score = models.FloatField()
    money = models.DecimalField(max_digits=20,decimal_places=2)

    def __str__():
        return self.name

class GuildMember(models.Model)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild)
