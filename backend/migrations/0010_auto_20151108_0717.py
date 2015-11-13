# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20151108_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='veteran',
            name='score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='veteran',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 2, 17, 36, 732733)),
        ),
    ]
