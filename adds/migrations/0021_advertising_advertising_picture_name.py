# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 20:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0020_auto_20160110_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertising',
            name='Advertising_picture_name',
            field=models.CharField(default=datetime.datetime(2016, 1, 9, 20, 37, 46, 740247, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]