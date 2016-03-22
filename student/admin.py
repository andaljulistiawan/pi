from django.contrib import admin
from student.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','registration_date']
    search_fields = ['name']
    list_filter = ['registration_date','courses']

admin.site.register(Student, StudentAdmin)