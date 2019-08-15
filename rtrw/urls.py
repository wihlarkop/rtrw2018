from django.conf.urls.static import static, settings
from django.contrib import admin
from django.urls import path, include

from rtrw.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls', namespace='warga')),
    path('surat/', include('suratpengantar.urls', namespace='surat')),
    path('akun/', include('akun.urls', namespace='akun')),
    path('index/', HomePageView.as_view(), name='index')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)