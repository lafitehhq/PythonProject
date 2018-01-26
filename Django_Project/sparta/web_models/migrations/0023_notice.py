# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0022_auto_20151009_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, '\u4e0d\u663e\u793a'), (1, '\u663e\u793a')])),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.CharField(max_length=256, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
                'db_table': 'Notice',
                'verbose_name_plural': '\u6700\u65b0\u516c\u544a\uff08\u5982\uff1a\u5f00\u73ed\u4fe1\u606f\uff09',
            },
            bases=(models.Model,),
        ),
    ]
