# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0011_auto_20151002_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='summary',
            field=models.CharField(default=b'summary', max_length=64),
            preserve_default=True,
        ),
    ]
