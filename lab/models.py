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
    genre = models.CharField(verbose_name=u'科研分类', choices=(('paper', '论文'), ('monograph', '专著')),
                             null=True, max_length=30)
    thesis = models.FileField(verbose_name=u'论文文件', upload_to='thesis/', max_length=100, null=True)
    prize = models.BooleanField(verbose_name=u'是否获奖', default=False)
    time = models.DateField(verbose_name=u'论文专著发表时间')

    class Meta:
        verbose_name = u'论文专著'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Information(models.Model):
    title = models.CharField(verbose_name=u'通知标题', max_length=50)
    content = models.TextField(verbose_name=u'通知内容')
    genre = models.CharField(verbose_name=u'通知类型', choices=(('news', '校内新闻'), ('lecture', '讲座信息'),
                                                            ('conference', '会议通知')), null=True, max_length=30)
    time = models.DateTimeField(default=datetime.now, verbose_name=u'通知发布时间')

    class Meta:
        verbose_name = u'信息通知'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Activity(models.Model):
    name = models.CharField(verbose_name=u'活动主题', max_length=50)
    desc = models.TextField(verbose_name=u'活动详情')
    genre = models.CharField(verbose_name=u'活动类型', choices=(('study', '学习'), ('entertainment', '娱乐')),
                             null=True, max_length=30)
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

class Prize(models.Model):
    name = models.CharField(verbose_name=u'奖项名称', max_length=100)
    desc = models.TextField(verbose_name=u'奖项详情')
    time = models.DateField(verbose_name=u'获奖时间')

    class Meta:
        verbose_name = u'实验室获奖'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TeacherProject(models.Model):
    teacher = models.ForeignKey(Teacher, verbose_name=u'教师')
    project = models.ForeignKey(Project, verbose_name=u'项目')

    class Meta:
        verbose_name = u'教师项目表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '教师'+str(self.teacher_id)+'项目'+str(self.project_id)


class TeacherResearch(models.Model):
    teacher = models.ForeignKey(Teacher, verbose_name=u'教师')
    research = models.ForeignKey(Research, verbose_name=u'科研')

    class Meta:
        verbose_name = u'教师科研表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '教师'+str(self.teacher_id)+'科研'+str(self.research_id)


class StudentProject(models.Model):
    student = models.ForeignKey(Student, verbose_name=u'学生')
    project = models.ForeignKey(Project, verbose_name=u'项目')

    class Meta:
        verbose_name = u'学生项目表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '学生'+str(self.student_id)+'项目'+str(self.project_id)


class StudentResearch(models.Model):
    student = models.ForeignKey(Student, verbose_name=u'学生')
    research = models.ForeignKey(Research, verbose_name=u'科研')

    class Meta:
        verbose_name = u'学生科研表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '学生' + str(self.student_id) + '科研' + str(self.research_id)