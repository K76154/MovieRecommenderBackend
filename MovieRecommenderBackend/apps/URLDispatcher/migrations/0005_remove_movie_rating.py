# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('URLDispatcher', '0004_auto_20170424_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='rating',
        ),
    ]
