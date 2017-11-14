# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0002_studentprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.CharField(max_length=200)),
                ('question', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
            ],
        ),
    ]
