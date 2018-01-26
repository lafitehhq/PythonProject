# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0015_student_studentdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetail',
            name='student',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentDetail',
        ),
    ]
