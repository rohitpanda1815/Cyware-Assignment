# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-04 14:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180604_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 4, 14, 17, 15, 186848), null=True),
        ),
    ]
