# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-04 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_customer_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('url_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='menus',
            field=models.ManyToManyField(blank=True, to='crm.Menu'),
        ),
    ]
