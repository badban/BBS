# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_bbs_event_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='location',
            field=models.CharField(blank=True, null=True, max_length=512, verbose_name='地点'),
        ),
        migrations.AlterField(
            model_name='bbs',
            name='event_leader',
            field=models.CharField(blank=True, null=True, max_length=512, verbose_name='活动发起人'),
        ),
    ]
