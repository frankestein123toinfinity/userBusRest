# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileDataApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busdatalist',
            name='busId',
        ),
        migrations.AlterField(
            model_name='busdatalist',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]