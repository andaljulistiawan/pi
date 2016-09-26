from __future__ import unicode_literals

from django.db import models
from student.models import Student

class Attendance(models.Model):
    name = models.ForeignKey(Student)
    checked_in = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now_add=True)



