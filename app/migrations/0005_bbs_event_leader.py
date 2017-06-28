# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170628_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='event_leader',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='最近活动日期'),
        ),
    ]
