# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_cost_per_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cost_per_month',
            field=models.FloatField(verbose_name='Cost Per Month'),
        ),
    ]
