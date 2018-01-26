# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0005_auto_20151002_0316'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]
