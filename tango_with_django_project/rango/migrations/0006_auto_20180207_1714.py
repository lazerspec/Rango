# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-07 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
