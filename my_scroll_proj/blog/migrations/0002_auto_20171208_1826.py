# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-08 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-published',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publish',
            new_name='published',
        ),
    ]
