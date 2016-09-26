from __future__ import unicode_literals

from django.db import models
from student.models import Student
from django.core.validators import MaxValueValidator, MinValueValidator
from course.models import Course

class Score(models.Model):
    name = models.ForeignKey(Student)
    courses = models.ManyToManyField(Course)
    ujian_praktik = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    ujian_tertulis = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])



# Create your models here.
