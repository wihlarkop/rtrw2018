from django.contrib import admin
from warga.models import Ktp, Kk


class KtpAdmin(admin.ModelAdmin):
    model = Ktp


class KkAdmin(admin.ModelAdmin):
    model = Kk


admin.site.register(Ktp, KtpAdmin)
admin.site.register(Kk, KkAdmin)