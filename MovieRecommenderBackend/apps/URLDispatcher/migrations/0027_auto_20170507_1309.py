# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 05:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('URLDispatcher', '0026_auto_20170507_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='ratingUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='URLDispatcher.RatingUser'),
        ),
    ]
