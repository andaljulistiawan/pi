from django.contrib import admin
from score.models import Score

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['name','ujian_praktik','ujian_tertulis','lulus']
    list_filter = ['name','courses']

    def lulus(self, instance):
        nilai_akhir = (instance.ujian_praktik * 0.7) + (instance.ujian_tertulis * 0.3)
        if nilai_akhir < 70:
            return 'Tidak Lulus'
        else:
            return 'Lulus'

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if request.user.groups.all()[0].name == 'Parents':
            return self.model._meta.get_all_field_names()

admin.site.register(Score, ScoreAdmin)