# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0020_recruit_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('href', models.CharField(default=b'javascript:void(0)', max_length=20, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe8\xbf\x9e\xe6\x8e\xa5')),
                ('logo', models.ImageField(upload_to=b'./static/images/student_pic/', verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aLOGO')),
                ('company', models.CharField(max_length=20, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'db_table': 'Cooperation',
                'verbose_name_plural': '\u4f01\u4e1a\u5408\u4f5c',
            },
            bases=(models.Model,),
        ),
    ]
