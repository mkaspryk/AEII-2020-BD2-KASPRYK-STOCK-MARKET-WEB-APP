from django.db import models
from currencies.app_settings import currencies
from decimal import Decimal, ROUND_HALF_UP
import json

class Currency(models.Model):
    id = models.TextField(primary_key=True, max_length=30, null=False)
    symbol = models.TextField(max_length=10)
    current_price = models.DecimalField(max_digits=20, decimal_places=2)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2)
    total_volume = models.DecimalField(max_digits=20, decimal_places=2)
    high_24h = models.DecimalField(max_digits=20, decimal_places=2)
    low_24h = models.DecimalField(max_digits=20, decimal_places=2)
    price_change_24h = models.DecimalField(max_digits=20, decimal_places=2)
    price_change_percentage_24h = models.FloatField()

    def convert_amount_to(self, amount, target_currency):
        ratio = self.current_price / target_currency.current_price
        return (amount * ratio).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)


class PriceTimeStamp(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    #bitcoin_price = models.DecimalField(max_digits=20, decimal_places=2)
    #ethereum_price = models.DecimalField(max_digits=20, decimal_places=2)
    #ripple_price = models.DecimalField(max_digits=20, decimal_places=2)
    #litecoin_price = models.DecimalField(max_digits=20, decimal_places=2)
    #tether_price = models.DecimalField(max_digits=20, decimal_places=2)
    #tezos_price = models.DecimalField(max_digits=20, decimal_places=2)
    #monero_price = models.DecimalField(max_digits=20, decimal_places=2)
    #eos_price = models.DecimalField(max_digits=20, decimal_places=2)
    #binancecoin_price = models.DecimalField(max_digits=20, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for currency in currencies:
            self.__setattr__(currency + "_price", models.DecimalField(max_digits=20, decimal_places=2))
        self.save()

    def to_json(self):
        diction = {}
        for currency in currencies:
            diction[currency] = float(getattr(self, currency+"_price"))
        #diction["ethereum"] = float(self.ethereum_price)
        #diction["ripple"] = float(self.ripple_price)
        #diction["litecoin"] = float(self.litecoin_price)
        #diction["tether"] = float(self.tether_price)
        #diction["tezos"] = float(self.tezos_price)
        #diction["monero"] = float(self.monero_price)
        #diction["eos"] = float(self.eos_price)
        #diction["binancecoin"] = float(self.binancecoin_price)
        return json.dumps(diction)

