# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 05:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biasapp', '0012_auto_20170326_0527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='negative',
        ),
        migrations.RemoveField(
            model_name='url',
            name='neutral',
        ),
        migrations.RemoveField(
            model_name='url',
            name='positive',
        ),
        migrations.RemoveField(
            model_name='url',
            name='text',
        ),
    ]
