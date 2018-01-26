# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0013_auto_20151002_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='weight',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='icon',
            field=models.ImageField(upload_to=b'./static/images/icon/', null=True, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(unique=True, max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, '\u4e0b\u7ebf'), (1, '\u4e0a\u7ebf')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='summary',
            field=models.CharField(default=b'summary', max_length=40, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b'),
            preserve_default=True,
        ),
    ]
