from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from django.db import transaction
import funds.models
from currencies.app_settings import currencies

# extending built-in User class:
class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def calculate_balance(self):
        funds = self.fund_set.all()
        sumofnums = Decimal(0)
        for fund in funds:
            sumofnums = sumofnums + fund.get_dollar_value()
        return sumofnums

    def is_solvent(self, pay_amount, pay_currency):
        try:
            fund = self.fund_set.get(currency=pay_currency)
            return fund.amount >= pay_amount
        except:
            return False

    @transaction.atomic('remote')
    def perform_transaction(self, pay_amount, pay_currency, buy_amount, buy_currency):
        try:
            with transaction.atomic('remote'):
                pay_fund = self.fund_set.get(currency=pay_currency)
                new_amount = pay_fund.amount - pay_amount
                pay_fund.amount = new_amount
                pay_fund.save()
                if self.fund_set.filter(currency=buy_currency).exists():
                    buy_fund = self.fund_set.get(currency=buy_currency)
                    buy_fund.amount = new_amount
                    buy_fund.save()
                else:
                    funds.models.Fund(owner=self, currency=buy_currency, amount=buy_amount).save()
        except:
            raise


@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        UserWallet.objects.create(user=instance)



