#-*-coding:utf-8-*-

from django.db import models
from django.contrib.auth.models import User

class BBS(models.Model):
    title = models.CharField(max_length=64, verbose_name='标题')
    summary = models.CharField(max_length=256, blank=True, null=True, verbose_name='摘要')
    content = models.TextField(verbose_name='内容')
    author = models.ForeignKey('BBS_user')
    category_id = models.ForeignKey('Category', default=1)
    view_count = models.IntegerField(verbose_name='浏览数')
    created_date = models.DateTimeField(verbose_name='发表时间')
    update_date = models.DateTimeField(verbose_name='最后修改时间')
    ranking = models.IntegerField(verbose_name='权重')
    imgnames = models.CharField(max_length=512,blank=True,null=True)
    allfilenames = models.CharField(max_length=512,blank=True,null=True)
    #rencent_event_date 最近活动日期
    recent_event_date = models.CharField(verbose_name='最近活动日期',max_length=512,blank=True,null=True)
    event_leader = models.CharField(verbose_name='活动发起人',max_length=512,blank=True,null=True)
    location = models.CharField(verbose_name='地点', max_length=512, blank=True, null=True)
    ebook_abstract = models.CharField(verbose_name='电子期刊摘要', max_length=512, blank=True, null=True)
    ebook_author = models.CharField(verbose_name='电子期刊作者', max_length=512, blank=True, null=True)
    ebook_isbn = models.CharField(verbose_name='期刊号', max_length=512, blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = verbose_name
        ordering = ['-id']

class Comment(models.Model):
    content = models.CharField(max_length=128, verbose_name='内容')
    user_id = models.ForeignKey('BBS_user', verbose_name='用户ID')
    article_id = models.ForeignKey('BBS', verbose_name='文章ID')
    date = models.DateTimeField(verbose_name='评论时间')
    is_read = models.BooleanField(default=0, verbose_name='是否已读')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='目录')
    administrator = models.ForeignKey('BBS_user', verbose_name='管理员')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = '节点'
        verbose_name_plural = verbose_name

class BBS_user(models.Model):
    username = models.CharField(max_length=16, verbose_name='用户名')
    password = models.CharField(max_length=16, verbose_name='密码')
    email = models.EmailField(default='example@email.com', verbose_name='邮箱')
    signature = models.CharField(max_length=128, default='这家伙很懒，什么也没留下.', verbose_name='个人简介')
    photo = models.ImageField(upload_to='upload_imgs/', default='upload_imgs/user-0.jpg', verbose_name='照片')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

