from django.contrib import admin
from .models import *


# Register your models here.

class AdvertisingAdmin(admin.ModelAdmin):
    # fields=['Advertising_header','Advertising_date','Advertising_text','Advertising_price']

    fieldsets = [
        ('Кратное описание', {'fields': ['Advertising_header']}),
        ('Стоимость', {'fields': ['Advertising_price']}),
        ('Текст объявления', {'fields': ['Advertising_text'], 'classes': ['collapse']}),
        ('Картинка', {'fields': ['Advertising_picture']})
        ]



    search_fields = ['Advertising_header']

class CommentAdmin(admin.ModelAdmin):
    fields=['comments_text', 'comments_advertising']

admin.site.register(Advertising, AdvertisingAdmin)
admin.site.register(Comments, CommentAdmin)