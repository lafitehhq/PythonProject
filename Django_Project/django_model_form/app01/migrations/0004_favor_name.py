# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20161228_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='favor',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]