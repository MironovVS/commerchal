# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0023_remove_advertising_advertising_picture_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertising',
            name='Advertising_picture',
            field=models.ImageField(blank=True, help_text='150x150px', null=True, upload_to='adds/static/images', verbose_name='Добавить картинку'),
        ),
    ]
