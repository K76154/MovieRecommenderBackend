# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 09:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('URLDispatcher', '0009_auto_20170501_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='link',
            new_name='links',
        ),
    ]
