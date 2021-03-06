# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0003_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default=0, max_length=120)),
                ('ques_paper_id', models.CharField(max_length=50)),
                ('marks', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('test_title', models.CharField(max_length=50)),
                ('client', models.CharField(default=None, max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
