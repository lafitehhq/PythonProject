# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0018_auto_20151002_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='detail',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
