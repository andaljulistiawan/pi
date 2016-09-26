from django.contrib import admin
from teacher.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'phone','registration_date']
    search_fields = ['id','name']
    list_filter = ['registration_date','courses']

admin.site.register(Teacher, TeacherAdmin)