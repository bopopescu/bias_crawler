# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biasapp', '0024_auto_20170327_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='text',
            field=models.CharField(default=None, max_length=10000),
        ),
    ]
