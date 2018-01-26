# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0006_delete_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0, choices=[(0, '\u4e0b\u7ebf'), (1, '\u4e0a\u7ebf')])),
                ('name', models.CharField(unique=True, max_length=32, db_index=True)),
            ],
            options={
                'db_table': 'Course',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
            bases=(models.Model,),
        ),
    ]
