# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-04 14:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180604_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 4, 14, 29, 0, 127527), null=True),
        ),
    ]
