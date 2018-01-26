# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0021_cooperation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperation',
            name='logo',
            field=models.ImageField(upload_to=b'./static/images/cooperation/', verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aLOGO'),
            preserve_default=True,
        ),
    ]
