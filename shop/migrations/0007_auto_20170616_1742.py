# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 12:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20170614_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='DOB',
            field=models.DateField(default=datetime.date(2017, 6, 16)),
        ),
        migrations.AlterField(
            model_name='seller',
            name='registeration_date',
            field=models.DateField(default=datetime.date(2017, 6, 16)),
        ),
    ]
