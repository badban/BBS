# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_bbs_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bbs',
            name='img',
        ),
        migrations.AddField(
            model_name='bbs',
            name='imgnames',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
