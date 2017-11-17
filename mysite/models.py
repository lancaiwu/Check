# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

#  执行  python manage.py makemigrations 命令会更新数据模型
#  执行  python manage.py migrate  命令 会自动创建表 ，表结构在 models 里面设置

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


# 复杂 数据 模型
# 两个表，Tag以Contact为外键，一个Contact可以对应多个Tag

class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField(default=0)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class CheckImage(models.Model):
    class Meta:
        db_table = 't_yz_img'  # 表名  若没有这个，则class 名则为表名

    id = models.AutoField(max_length=11, db_column='id', primary_key=True)  # 是主键 且自增
    img_name = models.CharField(max_length=256, db_column='img_name', blank=False)  # 是否可以为空
    img_path = models.CharField(max_length=560, db_column='img_path', blank=False)  # 是否可以为空
    img_left_top = models.IntegerField(max_length=11, db_column='img_left_top', blank=False)  # 是否可以为空
    img_right_top = models.IntegerField(max_length=11, db_column='img_right_top', blank=False)  # 是否可以为空
    img_right_bottom = models.IntegerField(max_length=11, db_column='img_right_bottom', blank=False)  # 是否可以为空
    img_left_bottom = models.IntegerField(max_length=11, db_column='img_left_bottom', blank=False)  # 是否允许为空
    time = models.IntegerField(max_length=13, db_column='time', blank=False)  # 是否允许为空
    left_index = models.IntegerField(max_length=4, db_column='left_index', blank=False, default=669)  # 默认值


class CheckImageRecord(models.Model):
    class Meta:
        db_table = 't_yz_record'

    id = models.AutoField(max_length=11, db_column='id', primary_key=True)
    phoneNumber = models.CharField(max_length=15, db_column='phoneNumber', blank=True)
    uid = models.CharField(max_length=11, db_column='uid', blank=True)
    imagePath1 = models.CharField(max_length=256, db_column='imagePath1', blank=False)
    imagePath2 = models.CharField(max_length=256, db_column='imagePath2', blank=False)
    checkResultType = models.IntegerField(max_length=11, db_column='checkResultType', blank=False)
    checkResult = models.IntegerField(max_length=11, db_column='checkResult', blank=False)
    time = models.IntegerField(max_length=20, db_column='time', blank=True)
