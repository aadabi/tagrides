# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0035_auto_20170517_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plannedtrips',
            name='driver_departure_latitude',
            field=models.FloatField(default=147, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plannedtrips',
            name='driver_departure_longitude',
            field=models.FloatField(default=104, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plannedtrips',
            name='driver_destination_latitude',
            field=models.FloatField(default=147, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plannedtrips',
            name='driver_destination_longitude',
            field=models.FloatField(default=107, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plannedtrips',
            name='driver_timeofdeparture_hour',
            field=models.IntegerField(default=24),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plannedtrips',
            name='driver_timeofdeparture_minute',
            field=models.IntegerField(default=60),
            preserve_default=False,
        ),
    ]