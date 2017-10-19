# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(verbose_name=u'昵称', max_length=30)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Note(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    title = models.CharField(verbose_name=u'帖子标题', max_length=50)
    content = models.TextField(verbose_name=u'帖子内容')
    time = models.DateTimeField(verbose_name=u'发帖时间', default=datetime.now)

    class Meta:
        verbose_name = u'帖子'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    note = models.ForeignKey(Note, verbose_name=u'评论的帖子')
    commentself = models.ForeignKey('self', null=True, blank=True)
    content = models.TextField(verbose_name=u'评论内容')
    time = models.DateTimeField(verbose_name=u'评论时间', default=datetime.now)

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '评论'+ str(self.id)