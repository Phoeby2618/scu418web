# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-27 02:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20171026_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='奖项名称')),
                ('desc', models.TextField(verbose_name='奖项详情')),
                ('time', models.DateField(verbose_name='获奖时间')),
            ],
            options={
                'verbose_name': '实验室获奖',
                'verbose_name_plural': '实验室获奖',
            },
        ),
        migrations.CreateModel(
            name='StudentProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Project', verbose_name='项目')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '学生项目表',
                'verbose_name_plural': '学生项目表',
            },
        ),
        migrations.CreateModel(
            name='StudentResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Research', verbose_name='科研')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '学生科研表',
                'verbose_name_plural': '学生科研表',
            },
        ),
        migrations.CreateModel(
            name='TeacherProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Project', verbose_name='项目')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Teacher', verbose_name='教师')),
            ],
            options={
                'verbose_name': '教师项目表',
                'verbose_name_plural': '教师项目表',
            },
        ),
        migrations.CreateModel(
            name='TeacherResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Research', verbose_name='科研')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Teacher', verbose_name='教师')),
            ],
            options={
                'verbose_name': '教师科研表',
                'verbose_name_plural': '教师科研表',
            },
        ),
    ]