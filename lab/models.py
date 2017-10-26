# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class Laboratory(models.Model):
    introduction = models.TextField(verbose_name=u'简介')
    research_area = models.TextField(verbose_name=u'研究方向')
    rules = models.TextField(verbose_name=u'规章制度')

    class Meta:
        verbose_name = u'实验室简介'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '实验室'


class Teacher(models.Model):
    name = models.CharField(verbose_name=u'教师姓名', max_length=20)
    profession = models.CharField(verbose_name=u'职称', choices=(('professor', '教授'), ('associate', '副教授'),
                                                               ('lecturer', '讲师')), max_length=20)
    department = models.CharField(verbose_name=u'系所', max_length=50)
    email = models.CharField(verbose_name=u'邮箱', max_length=50)
    individual = models.TextField(verbose_name=u'个人简介')
    photo = models.ImageField(verbose_name=u'教师照片', upload_to='photo/', max_length=100)

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(verbose_name=u'学生姓名', max_length=20)
    degree = models.CharField(verbose_name=u'学位', max_length=10, choices=(('bachelor', '学士'), ('master', '硕士'), ('doctor', '博士')))
    graduate = models.BooleanField(verbose_name=u'是否毕业', default=False)
    job = models.CharField(verbose_name=u'毕业去向', max_length=50, default=u'')
    individual = models.TextField(verbose_name=u'个人简介')
    photo = models.ImageField(verbose_name=u'学生照片', upload_to='photo/', max_length=100)

    class Meta:
        verbose_name = u'学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(verbose_name=u'项目名称', max_length=50)
    content = models.TextField(verbose_name=u'项目详情')
    time = models.DateField(verbose_name=u'项目开始时间')
    finish = models.BooleanField(verbose_name=u'项目是否已经完成', default=True)

    class Meta:
        verbose_name = u'项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Research(models.Model):
    name = models.CharField(verbose_name=u'论文专著名称', max_length=50)
    content = models.TextField(verbose_name=u'论文专著详情')
    time = models.DateField(verbose_name=u'论文专著发表时间')

    class Meta:
        verbose_name = u'论文专著'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Information(models.Model):
    title = models.CharField(verbose_name=u'通知标题', max_length=50)
    content = models.TextField(verbose_name=u'通知内容')
    time = models.DateTimeField(default=datetime.now, verbose_name=u'通知发布时间')

    class Meta:
        verbose_name = u'信息通知'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Activity(models.Model):
    name = models.CharField(verbose_name=u'活动主题', max_length=50)
    desc = models.TextField(verbose_name=u'活动详情')
    time = models.DateField(verbose_name=u'活动时间')

    class Meta:
        verbose_name = u'活动'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
    
    
 class Image(models.Model):
    activity = models.ForeignKey(Activity, verbose_name=u'活动')
    name = models.CharField(verbose_name=u'图片名称', max_length=30)
    photo = models.ImageField(verbose_name=u'活动图片', upload_to='image/', max_length=100)

    class Meta:
        verbose_name = u'活动图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Resource(models.Model):
    resource_name = models.CharField(verbose_name=u'资源名称', max_length=30)
    author_name = models.CharField(verbose_name=u'上传者姓名', max_length=20)
    desc = models.TextField(verbose_name=u'资源描述')
    path = models.FileField(verbose_name=u'文件保存路径', upload_to='uploads/', max_length=100)
    time = models.DateField(verbose_name=u'文件上传时间')

    class Meta:
        verbose_name = u'学习资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.resource_name
