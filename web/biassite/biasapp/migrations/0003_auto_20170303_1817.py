# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biasapp', '0002_articles_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
