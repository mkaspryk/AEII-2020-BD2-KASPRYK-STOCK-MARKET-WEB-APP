from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save


class GuildMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    guild = models.ForeignKey('crypto_guilds.Guild', on_delete=models.SET_NULL, default=None, null=True)

    @receiver(post_save, sender=User)
    def create_user_guildmember(sender, instance, created, **kwargs):
        if created:
            GuildMember.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_guildmember(sender, instance, **kwargs):
        instance.guildmember.save()

class Guild(models.Model):
    guild_name = models.CharField(max_length=50, blank = False)
    master = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    max_members = models.IntegerField(blank = False, validators=[MaxValueValidator(50),MinValueValidator(1)])
    score = models.IntegerField(default = 0)
    money = models.DecimalField(max_digits=20,decimal_places=2, blank = False)
