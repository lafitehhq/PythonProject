# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0023_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.CharField(max_length=256, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b'),
            preserve_default=True,
        ),
    ]
