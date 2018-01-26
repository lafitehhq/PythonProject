# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0009_course_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.IntegerField(default=1, choices=[(0, '\u4e0b\u7ebf'), (1, '\u4e0a\u7ebf')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='summary',
            field=models.CharField(default=b'summary', max_length=128),
            preserve_default=True,
        ),
    ]
