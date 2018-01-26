# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0024_auto_20151009_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='detail',
            field=models.TextField(null=True, verbose_name=b'\xe5\x85\xac\xe5\x91\x8a\xe8\xaf\xa6\xe7\xbb\x86', blank=True),
            preserve_default=True,
        ),
    ]
