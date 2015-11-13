# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queueentry',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 1, 5, 34, 795382)),
        ),
    ]
