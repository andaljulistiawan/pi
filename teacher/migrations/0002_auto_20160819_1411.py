# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-19 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.AutoField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]