# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0012_comments_comments_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('pic', models.ImageField(upload_to='', verbose_name='картинка')),
                ('alias', models.SlugField(verbose_name='Alias картинки')),
                ('img_advertising', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adds.Advertising')),
            ],
            options={
                'verbose_name_plural': 'Картинки',
                'verbose_name': 'Картинка',
            },
        ),
    ]
