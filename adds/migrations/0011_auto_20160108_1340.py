# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0010_auto_20160108_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comments_article',
            new_name='comments_advertising',
        ),
    ]
