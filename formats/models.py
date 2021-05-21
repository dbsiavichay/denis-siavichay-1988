from django.db import models
from django_countries.fields import CountryField


class Currency(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=2)

    def __str__(self):
        return self.code


class Format(models.Model):
    country = CountryField()
    currency = models.ForeignKey(
        Currency, on_delete=models.PROTECT,
    )