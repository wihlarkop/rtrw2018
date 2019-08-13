from django.contrib import admin
from warga.models import Ktp, Kk, Ktpkk


class KtpAdmin(admin.ModelAdmin):
    model = Ktp


class KkAdmin(admin.ModelAdmin):
    model = Kk


class KtpkkAdmin(admin.ModelAdmin):
    model = Ktpkk


admin.site.register(Ktp, KtpAdmin)
admin.site.register(Kk, KkAdmin)
admin.site.register(Ktpkk, KtpkkAdmin)