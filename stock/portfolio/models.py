from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from currencies.app_settings import currencies
# todo rename portfolio to wallet, UserStock to UserWallet
# todo every user has a user_wallet, user_wallet contains *funds* of many different cryptos

# extending built-in User class:
class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def calculate_balance(self):
        funds = self.fund_set.all()
        sumofnums = Decimal(0)
        for fund in funds:
            sumofnums = sumofnums + fund.get_dollar_value()
        return sumofnums

@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        UserWallet.objects.create(user=instance)



