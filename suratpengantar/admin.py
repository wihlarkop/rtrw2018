from django.contrib import admin
from suratpengantar.models import Suratpengantar

class SuratAdmin(admin.ModelAdmin):
    model = Suratpengantar

admin.site.register(Suratpengantar, SuratAdmin)

