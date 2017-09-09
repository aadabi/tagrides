# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0032_auto_20170516_0557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driveractive',
            name='driverod_departure',
        ),
        migrations.RemoveField(
            model_name='driveractive',
            name='driverod_destination',
        ),
        migrations.AddField(
            model_name='driveractive',
            name='driverod_departure_lat',
            field=models.FloatField(default=147, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driveractive',
            name='driverod_departure_lon',
            field=models.FloatField(default=105, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driveractive',
            name='driverod_destination_lat',
            field=models.FloatField(default=147, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driveractive',
            name='driverod_destination_lon',
            field=models.FloatField(default=104, max_length=200),
            preserve_default=False,
        ),
    ]
