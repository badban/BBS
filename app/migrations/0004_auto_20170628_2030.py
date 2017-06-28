# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170625_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='allfilenames',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='bbs',
            name='recent_event_date',
            field=models.CharField(blank=True, max_length=512, verbose_name='最近活动日期', null=True),
        ),
    ]
