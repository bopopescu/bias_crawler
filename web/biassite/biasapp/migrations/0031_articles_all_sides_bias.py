# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-28 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biasapp', '0030_auto_20170425_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='all_sides_bias',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
    ]
