# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newshome', '0009_article_article_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_summary',
            field=models.TextField(default='I wil put in shit, wait! '),
        ),
    ]