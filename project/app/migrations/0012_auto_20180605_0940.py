# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-05 09:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180605_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 5, 9, 40, 1, 517243), null=True),
        ),
    ]
