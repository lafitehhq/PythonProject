# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bxslider',
            name='name',
        ),
    ]
