# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0018_auto_20160110_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertising',
            name='Advertising_picture',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Добавить картинку'),
        ),
    ]