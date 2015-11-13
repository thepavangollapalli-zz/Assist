# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QueueEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_name', models.CharField(max_length=100)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 11, 6, 0, 38, 6, 531386))),
                ('question', models.TextField()),
                ('queue', models.ForeignKey(related_name='entries', to='backend.Queue')),
            ],
        ),
    ]
