from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    cost_per_month = models.FloatField(verbose_name='Cost Per Month')

    def __str__(self):
        return self.name