# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0017_student_studentdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, '\u5df2\u8fc7\u671f'), (1, '\u62db\u8058\u4e2d')])),
                ('title', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=20)),
                ('detail', models.CharField(max_length=20)),
                ('deadline', models.DateField()),
            ],
            options={
                'db_table': 'Recruit',
                'verbose_name_plural': '\u62db\u8058\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='studentdetail',
            options={'verbose_name_plural': '\u5b66\u751f\u66f4\u591a\u4fe1\u606f'},
        ),
    ]
