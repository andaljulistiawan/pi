from django.contrib import admin
from course.models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name','cost_per_month']

    def cost_per_month(self, instance):
        return 'IDR {:,}'.format(instance.cost).replace(',', '.')
admin.site.register(Course, CourseAdmin)
