# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-26 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20161226_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
