# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 05:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('URLDispatcher', '0023_auto_20170507_1304'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='RatingUser',
        ),
    ]