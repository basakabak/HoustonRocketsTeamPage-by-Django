# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rockets', '0005_auto_20171226_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seating_map',
            field=models.ImageField(blank=True, upload_to='imgs'),
        ),
    ]
