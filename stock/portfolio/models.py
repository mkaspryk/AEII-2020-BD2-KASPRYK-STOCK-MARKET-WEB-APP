from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from currencies.app_settings import currencies
# todo rename portfolio to wallet, UserStock to UserWallet

# extending built-in User class:
class UserStock(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    #cena_bitcoin = models.DecimalField(max_digits=20, decimal_places=2)
    def __init__(self):
        setattr(UserStock, 'cena_bitcoin', models.DecimalField(max_digits=20, decimal_places=2))




@receiver(post_save, sender=User)
def create_user_stock(sender, instance, created, **kwargs):
    if created:
        print("creating user_stock")
        UserStock.objects.create(user=instance)


class Stock(models.Model):
    owner = models.ForeignKey(UserStock, on_delete=models.DO_NOTHING)
    currency = models.ForeignKey('currencies.Currency', on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def get_value(self):
        return self.amount * self.currency.price
