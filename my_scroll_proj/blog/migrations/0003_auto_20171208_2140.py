# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-08 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171208_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='published', verbose_name='Slug'),
        ),
    ]
