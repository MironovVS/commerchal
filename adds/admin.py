from django.contrib import admin
from .models import *


# Register your models here.

class AdvertisingAdmin(admin.ModelAdmin):
    # fields=['Advertising_header','Advertising_date','Advertising_text','Advertising_price']

    fieldsets = [
        ('Кратное описание', {'fields': ['Advertising_header']}),
        ('Стоимость', {'fields': ['Advertising_price']}),
        ('Текст объявления', {'fields': ['Advertising_text'], 'classes': ['collapse']})
        ]



    search_fields = ['Advertising_header']


admin.site.register(Advertising, AdvertisingAdmin)
