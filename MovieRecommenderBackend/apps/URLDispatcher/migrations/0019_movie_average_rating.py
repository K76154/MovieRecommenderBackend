# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLDispatcher', '0018_auto_20170502_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='average_rating',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]