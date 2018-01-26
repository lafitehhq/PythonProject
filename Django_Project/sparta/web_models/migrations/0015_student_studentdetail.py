# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0014_auto_20151002_0402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, '\u4e0b\u7ebf'), (1, '\u4e0a\u7ebf')])),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('pic', models.ImageField(upload_to=b'./static/images/student_pic/', null=True, verbose_name=b'\xe5\xad\xa6\xe5\x91\x98\xe5\xa4\xb4\xe5\x83\x8f', blank=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', db_index=True)),
                ('company', models.CharField(max_length=32, verbose_name=b'\xe5\xb0\xb1\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('salary', models.CharField(max_length=32, verbose_name=b'\xe8\x96\xaa\xe6\xb0\xb4')),
            ],
            options={
                'db_table': 'Student',
                'verbose_name_plural': '\u5b66\u751f\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('letter_of_thanks', models.CharField(max_length=256, verbose_name=b'\xe5\xad\xa6\xe5\x91\x98\xe6\x84\x9f\xe8\xb0\xa2\xe4\xbf\xa1')),
                ('student', models.OneToOneField(to='web_models.Student')),
            ],
            options={
                'db_table': 'Student',
                'verbose_name_plural': '\u5b66\u751f\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
    ]
