# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20151107_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queueentry',
            name='queue',
        ),
        migrations.AddField(
            model_name='veteran',
            name='problem',
            field=models.CharField(max_length=15, default='none'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Queue',
        ),
        migrations.DeleteModel(
            name='QueueEntry',
        ),
    ]
