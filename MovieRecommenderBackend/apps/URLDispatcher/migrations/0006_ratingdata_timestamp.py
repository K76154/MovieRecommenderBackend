# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLDispatcher', '0005_remove_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingdata',
            name='timestamp',
            field=models.BigIntegerField(null=True),
        ),
    ]
