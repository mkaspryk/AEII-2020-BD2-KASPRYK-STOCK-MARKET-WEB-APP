from django.db import models


class Currency(models.Model):
    full_name = models.TextField(max_length=20, null=True)
    short_name = models.TextField(max_length=10, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.DecimalField(max_digits=20, decimal_places=2)
    circulating_supply = models.DecimalField(max_digits=20, decimal_places=2)
    change_24h = models.FloatField()


class BitcoinPrice(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2)

class EthereumPrice(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2)
