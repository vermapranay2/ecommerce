# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170614_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]