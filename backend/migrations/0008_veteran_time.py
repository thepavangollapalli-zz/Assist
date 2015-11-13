# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20151108_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='veteran',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 2, 0, 54, 94991)),
        ),
    ]
