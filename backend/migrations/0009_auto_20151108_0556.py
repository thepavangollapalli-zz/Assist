# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_veteran_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veteran',
            name='ssn',
        ),
        migrations.AlterField(
            model_name='veteran',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 0, 56, 22, 767487)),
        ),
    ]
