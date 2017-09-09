# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-19 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0055_ridehistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='car_color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='driver_license',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_car',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]