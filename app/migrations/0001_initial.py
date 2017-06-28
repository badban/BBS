# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BBS',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('summary', models.CharField(null=True, max_length=256, verbose_name='摘要', blank=True)),
                ('content', models.TextField(verbose_name='内容')),
                ('view_count', models.IntegerField(verbose_name='浏览数')),
                ('created_date', models.DateTimeField(verbose_name='发表时间')),
                ('update_date', models.DateTimeField(verbose_name='最后修改时间')),
                ('ranking', models.IntegerField(verbose_name='权重')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name_plural': '帖子',
                'verbose_name': '帖子',
            },
        ),
        migrations.CreateModel(
            name='BBS_user',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('username', models.CharField(max_length=16, verbose_name='用户名')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, default='example@email.com', verbose_name='邮箱')),
                ('signature', models.CharField(max_length=128, default='这家伙很懒，什么也没留下.', verbose_name='个人简介')),
                ('photo', models.ImageField(default='upload_imgs/user-0.jpg', verbose_name='照片', upload_to='upload_imgs/')),
            ],
            options={
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='目录')),
                ('administrator', models.ForeignKey(to='app.BBS_user', verbose_name='管理员')),
            ],
            options={
                'verbose_name_plural': '节点',
                'verbose_name': '节点',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('content', models.CharField(max_length=128, verbose_name='内容')),
                ('date', models.DateTimeField(verbose_name='评论时间')),
                ('is_read', models.BooleanField(default=0, verbose_name='是否已读')),
                ('article_id', models.ForeignKey(to='app.BBS', verbose_name='文章ID')),
                ('user_id', models.ForeignKey(to='app.BBS_user', verbose_name='用户ID')),
            ],
            options={
                'verbose_name_plural': '评论',
                'verbose_name': '评论',
            },
        ),
        migrations.AddField(
            model_name='bbs',
            name='author',
            field=models.ForeignKey(to='app.BBS_user'),
        ),
        migrations.AddField(
            model_name='bbs',
            name='category_id',
            field=models.ForeignKey(default=1, to='app.Category'),
        ),
    ]
