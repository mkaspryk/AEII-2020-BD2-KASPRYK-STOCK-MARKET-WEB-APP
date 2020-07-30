from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from currencies.models import Currency
from decimal import Decimal, ROUND_HALF_UP

@receiver(post_save, sender='portfolio.UserWallet')
def add_initial_funds(sender, instance, created, **kwargs):
    if created:
        StockFund.objects.create(owner=instance, currency=Currency.objects.get(name="bitcoin"), amount=1.00)


class StockFund(models.Model):
    name = models.CharField(max_length = 40)
    currency = models.ForeignKey('currencies.Currency', on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def get_dollar_value_unrounded(self):
        amount_val = self.amount
        price_val = self.currency.current_price
        val = amount_val * price_val
        return val

    def get_dollar_value(self):
        unrounded = self.get_dollar_value_unrounded()
        return unrounded.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)  # returns rounded value intentionally

    def add_fund_value(self, changed_amount):
        amount = amount + changed_amount
        


class StockFundUser(models.Model):
	stockfundname = models.ForeignKey('StockFund', on_delete=models.CASCADE)
	isOwner = models.BooleanField(default=False)
	name = models.CharField(max_length = 40)
	wallet = models.ForeignKey('portfolio.UserWallet', on_delete=models.DO_NOTHING, default = "")
	def add_wallet_value(self, changed_amount):
		pay_fund = self.fund_set.get(currency=self.stockfundname.currency)
		new_amount = pay_fund.amount + changed_amount
		pay_fund.amount = new_amount
		pay_fund.save()



