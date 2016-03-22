from django.contrib import admin
from course.models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','cost_per_month']

admin.site.register(Course, CourseAdmin)
