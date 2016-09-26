# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-16 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0003_auto_20160322_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('registration_date', models.DateField()),
                ('courses', models.ManyToManyField(to='course.Course')),
            ],
        ),
    ]
