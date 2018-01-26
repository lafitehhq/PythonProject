# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BxSlider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0, choices=[(0, '\u4e0b\u7ebf'), (1, '\u4e0a\u7ebf')])),
                ('name', models.CharField(default=b'unname', max_length=32, db_index=True)),
                ('img', models.ImageField(upload_to=b'./static/images/focus/')),
                ('href', models.CharField(max_length=256)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'BxSlider',
                'verbose_name_plural': '\u9996\u9875\u8f6e\u64ad',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0, choices=[(0, '\u4e0b\u7ebf'), (1, '\u4e0a\u7ebf')])),
                ('name', models.CharField(default=b'unname', max_length=32, db_index=True)),
            ],
            options={
                'db_table': 'Course',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
            bases=(models.Model,),
        ),
    ]
