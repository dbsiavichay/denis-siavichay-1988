from django.contrib import admin

from .models import Currency, Format

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "symbol")

@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = (
        "country", "currency", "show", "display", "get_format"
    )