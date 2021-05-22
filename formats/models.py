from django.db import models
from django_countries.fields import CountryField


class Currency(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=2)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ("code",)


class Format(models.Model):
    class Show(models.IntegerChoices):
        CODE = 1, "Code"
        SYMBOL = 2, "Symbol"

    class Display(models.IntegerChoices):
        AFTER = 1, "After price"
        BEFORE = 2, "Before price"

    class Delimiter(models.TextChoices):
        COMMA = ","
        DOT = "."

    country = CountryField()
    currency = models.ForeignKey(
        Currency, on_delete=models.PROTECT,
    )
    show = models.PositiveSmallIntegerField(
        choices=Show.choices, default=Show.CODE
    )
    display = models.PositiveSmallIntegerField(
        choices=Display.choices, default=Display.AFTER
    )
    cents = models.BooleanField(
        verbose_name="show cents?"
    )
    thousand_delimiter = models.CharField(
        max_length=2, choices=Delimiter.choices,
        default=Delimiter.COMMA
    )

    def __str__(self):
        return self.get_format()

    
