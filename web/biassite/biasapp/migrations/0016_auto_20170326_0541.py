# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biasapp', '0015_auto_20170326_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='negative',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='url',
            name='neutral',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='url',
            name='positive',
            field=models.IntegerField(default=None),
        ),
    ]