# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0019_auto_20151002_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='weight',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89'),
            preserve_default=True,
        ),
    ]
