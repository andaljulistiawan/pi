# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-16 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20160816_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='no_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
