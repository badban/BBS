# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170628_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='ebook_abstract',
            field=models.CharField(max_length=512, null=True, verbose_name='电子期刊摘要', blank=True),
        ),
        migrations.AddField(
            model_name='bbs',
            name='ebook_author',
            field=models.CharField(max_length=512, null=True, verbose_name='电子期刊作者', blank=True),
        ),
        migrations.AddField(
            model_name='bbs',
            name='ebook_isbn',
            field=models.CharField(max_length=512, null=True, verbose_name='期刊号', blank=True),
        ),
    ]
