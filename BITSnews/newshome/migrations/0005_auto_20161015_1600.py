# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newshome', '0004_auto_20161015_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_video',
            field=models.CharField(max_length=200),
        ),
    ]
