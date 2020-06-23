from django.db import models
import json

class Currency(models.Model):
    full_name = models.TextField(max_length=20, null=True)
    short_name = models.TextField(max_length=10, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.DecimalField(max_digits=20, decimal_places=2)
    circulating_supply = models.DecimalField(max_digits=20, decimal_places=2)
    change_24h = models.FloatField()


class PriceTimeStamp(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    btc_price = models.DecimalField(max_digits=20, decimal_places=2)
    eth_price = models.DecimalField(max_digits=20, decimal_places=2)
    xrp_price = models.DecimalField(max_digits=20, decimal_places=2)
    ltc_price = models.DecimalField(max_digits=20, decimal_places=2)
    usdt_price = models.DecimalField(max_digits=20, decimal_places=2)
    libra_price = models.DecimalField(max_digits=20, decimal_places=2)
    xmr_price = models.DecimalField(max_digits=20, decimal_places=2)
    eos_price = models.DecimalField(max_digits=20, decimal_places=2)
    bnb_price = models.DecimalField(max_digits=20, decimal_places=2)

    def to_json(self):
        diction = {}
        diction["btc"] = float(self.btc_price)
        diction["eth"] = float(self.eth_price)
        diction["xrp"] = float(self.xrp_price)
        diction["ltc"] = float(self.ltc_price)
        diction["usdt"] = float(self.usdt_price)
        diction["libra"] = float(self.libra_price)
        diction["xmr"] = float(self.xmr_price)
        diction["eos"] = float(self.eos_price)
        diction["bnb"] = float(self.bnb_price)
        return json.dumps(diction)

