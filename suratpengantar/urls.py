from django.urls import path
from suratpengantar.views import (SuratCreate, SuratList, SuratDelete, SuratDetail, SuratUpdate)

app_name = 'suratpengantar'

urlpatterns = [
    path('list/', SuratList.as_view(), name='list_surat'),
    path('create/', SuratCreate.as_view(), name='create_surat'),
    path('update/<pk>', SuratUpdate.as_view(), name='update_surat'),
    path('delete/<pk>', SuratDelete.as_view(), name='delete_surat'),
    path('detail/<pk>', SuratDetail.as_view(), name='detail_surat'),
]
