from __future__ import unicode_literals

from django.db import models
from course.models import Course

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    courses = models.ManyToManyField(Course)
    registration_date = models.DateField()

    def __str__(self):
        return self.name