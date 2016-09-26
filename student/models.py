from __future__ import unicode_literals

from django.db import models
from course.models import Course

class Student(models.Model):
    id = models.AutoField(primary_key=True,max_length=20,unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    courses = models.ManyToManyField(Course)
    registration_date = models.DateField()

    @staticmethod
    def autocomplete_search_fields():
        return 'name',

    def __str__(self):
        return self.name