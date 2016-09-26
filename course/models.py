from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=30)
    cost = models.IntegerField()

    def __str__(self):
        return self.name