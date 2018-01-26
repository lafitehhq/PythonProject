# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0002_remove_bxslider_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bxslider',
            name='name',
            field=models.CharField(default=b'unname', max_length=32, db_index=True),
            preserve_default=True,
        ),
    ]
