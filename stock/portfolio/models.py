from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from currencies.app_settings import currencies
# todo rename portfolio to wallet, UserStock to UserWallet
# todo every user has a user_wallet, user_wallet contains *funds* of many different cryptos

# extending built-in User class:
class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)


@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        UserWallet.objects.create(user=instance)



