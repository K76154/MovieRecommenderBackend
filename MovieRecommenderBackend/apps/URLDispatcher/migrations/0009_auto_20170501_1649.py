# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLDispatcher', '0008_auto_20170501_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='links',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='action',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='adventure',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='animation',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='children',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='comedy',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='crime',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='documentary',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='drama',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='fantasy',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='filmnoir',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='horror',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='musical',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='mystery',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='romance',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='scifi',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='thriller',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='unknown',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='video_date',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='war',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='western',
        ),
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateField(),
        ),
    ]