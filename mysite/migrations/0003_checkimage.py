# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_contact_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckImage',
            fields=[
                ('id', models.AutoField(db_column='id', max_length=11, primary_key=True, serialize=False)),
                ('img_name', models.CharField(db_column='img_name', max_length=256)),
                ('img_path', models.CharField(db_column='img_path', max_length=560)),
                ('img_left_top', models.IntegerField(db_column='img_left_top', max_length=11)),
                ('img_right_top', models.IntegerField(db_column='img_right_top', max_length=11)),
                ('img_right_bottom', models.IntegerField(db_column='img_right_bottom', max_length=11)),
                ('img_left_bottom', models.IntegerField(db_column='img_left_bottom', max_length=11)),
                ('time', models.IntegerField(db_column='time', max_length=13)),
                ('left_index', models.IntegerField(db_column='left_index', default=669, max_length=4)),
            ],
            options={
                'db_table': 't_yz_img',
            },
        ),
    ]