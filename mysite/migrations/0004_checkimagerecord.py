# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_checkimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckImageRecord',
            fields=[
                ('id', models.AutoField(db_column='id', max_length=11, primary_key=True, serialize=False)),
                ('phoneNumber', models.CharField(blank=True, db_column='phoneNumber', max_length=15)),
                ('uid', models.CharField(blank=True, db_column='uid', max_length=11)),
                ('imagePath1', models.CharField(db_column='imagePath1', max_length=256)),
                ('imagePath2', models.CharField(db_column='imagePath2', max_length=256)),
                ('checkResultType', models.IntegerField(db_column='checkResultType', max_length=11)),
                ('checkResult', models.IntegerField(db_column='checkResult', max_length=11)),
                ('time', models.IntegerField(blank=True, db_column='time', max_length=20)),
            ],
            options={
                'db_table': 't_yz_record',
            },
        ),
    ]
