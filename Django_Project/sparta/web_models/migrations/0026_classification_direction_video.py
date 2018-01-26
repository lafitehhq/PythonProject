# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0025_notice_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'db_table': 'Classification',
                'verbose_name_plural': '\u5206\u7c7b\uff08\u89c6\u9891\u5206\u7c7b\uff09',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('classification', models.ManyToManyField(to='web_models.Classification')),
            ],
            options={
                'db_table': 'Direction',
                'verbose_name_plural': '\u65b9\u5411\uff08\u89c6\u9891\u65b9\u5411\uff09',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, '\u4e0b\u7ebf'), (1, '\u4e0a\u7ebf')])),
                ('level', models.IntegerField(default=1, verbose_name=b'\xe7\xba\xa7\xe5\x88\xab', choices=[(1, '\u521d\u7ea7'), (2, '\u4e2d\u7ea7'), (3, '\u9ad8\u7ea7')])),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('summary', models.CharField(max_length=32, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('img', models.ImageField(upload_to=b'./static/images/Video/', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('href', models.CharField(max_length=256, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe5\x9c\xb0\xe5\x9d\x80')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Video',
                'verbose_name_plural': '\u89c6\u9891',
            },
            bases=(models.Model,),
        ),
    ]
