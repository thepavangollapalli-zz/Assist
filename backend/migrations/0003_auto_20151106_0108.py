# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20151106_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queueentry',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 1, 8, 49, 219649)),
        ),
    ]
