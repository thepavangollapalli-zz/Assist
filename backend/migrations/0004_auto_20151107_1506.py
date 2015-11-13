# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20151106_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='choices',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Veteran',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default=None)),
                ('age', models.CharField(max_length=3)),
                ('ssn', models.CharField(max_length=11)),
                ('bday', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='queueentry',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 15, 6, 11, 520725)),
        ),
    ]
