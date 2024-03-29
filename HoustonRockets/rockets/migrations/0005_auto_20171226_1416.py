# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rockets', '0004_ticket_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='arena',
            field=models.CharField(blank=True, default='Texas', max_length=80),
        ),
        migrations.AlterField(
            model_name='match',
            name='lat',
            field=models.FloatField(blank=True, default=29.751003),
        ),
        migrations.AlterField(
            model_name='match',
            name='lng',
            field=models.FloatField(blank=True, default=-95.362122),
        ),
        migrations.AlterField(
            model_name='match',
            name='video',
            field=models.CharField(default='kNst9WrrJRA', max_length=300),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='seating_map',
            field=models.ImageField(default='rockets/static/assets/images/seating_map.jpg', upload_to='imgs'),
        ),
    ]
