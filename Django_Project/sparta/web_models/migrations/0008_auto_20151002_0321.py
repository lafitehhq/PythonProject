# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0007_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='summary',
            field=models.CharField(default=b'summary', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bxslider',
            name='status',
            field=models.IntegerField(default=1, choices=[(0, '\u4e0b\u7ebf'), (1, '\u4e0a\u7ebf')]),
            preserve_default=True,
        ),
    ]
