from django.contrib import admin
from attendance.models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['name', 'checked_in']
    list_filter = ['name', 'checked_in']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if request.user.groups.all()[0].name == 'Parents':
            return self.model._meta.get_all_field_names()


admin.site.register(Attendance, AttendanceAdmin)