from django.db import models
from django.contrib.auth.models import User


# extending built-in User class:
class UserStock(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def get_value(self):
        sum = 0
        for stock in self.stock_set:
            sum = sum + stock.get_value()
        return sum


class Stock(models.Model):
    owner = models.ForeignKey(UserStock, on_delete=models.DO_NOTHING)
    currency = models.ForeignKey('currencies.Currency', on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def get_value(self):
        return self.amount * self.currency.price
