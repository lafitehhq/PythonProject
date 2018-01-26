# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0026_classification_direction_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='classification',
            field=models.ForeignKey(blank=True, to='web_models.Classification', null=True),
            preserve_default=True,
        ),
    ]
