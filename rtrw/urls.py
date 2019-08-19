from django.conf.urls.static import static, settings
from django.contrib import admin
from django.urls import path, include

from rtrw.views import HomePageView,SuratUserCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls', namespace='warga')),
    path('surat/', include('suratpengantar.urls', namespace='surat')),
    path('akun/', include('akun.urls', namespace='akun')),
    path('', HomePageView.as_view(), name='index'),
    path('surat/', SuratUserCreate.as_view(), name='surat_user')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)