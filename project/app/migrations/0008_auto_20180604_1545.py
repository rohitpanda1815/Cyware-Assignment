# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-04 15:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180604_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email1',
        ),
        migrations.AlterField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 4, 15, 45, 42, 572640), null=True),
        ),
    ]