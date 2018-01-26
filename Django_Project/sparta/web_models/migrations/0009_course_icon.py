# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0008_auto_20151002_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='icon',
            field=models.ImageField(null=True, upload_to=b'./static/images/icon/', blank=True),
            preserve_default=True,
        ),
    ]
