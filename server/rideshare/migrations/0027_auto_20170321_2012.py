# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0026_auto_20170321_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='rideractive',
            name='driverod_departure',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rideractive',
            name='driverod_destination',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
