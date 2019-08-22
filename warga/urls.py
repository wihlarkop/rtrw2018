from django.urls import path
from warga.views import (KtpCreate, KtpList, KtpDetail, KtpDelete, KtpUpdate,
                         KkCreate, KkList, KkDelete, KkUpdate, KkDetail)

app_name = 'warga'

urlpatterns = [
    # ktp route
    path('ktp/list', KtpList.as_view(), name='list_ktp'),
    path('ktp/list/search', KtpList.as_view(), name='search_ktp'),
    path('ktp/create/', KtpCreate.as_view(), name='create_ktp'),
    path('ktp/update/<pk>', KtpUpdate.as_view(), name='update_ktp'),
    path('ktp/delete/<pk>', KtpDelete.as_view(), name='delete_ktp'),
    path('ktp/detail/<pk>', KtpDetail.as_view(), name='detail_ktp'),
    # kk route
    path('kk/list', KkList.as_view(), name='list_kk'),
    path('ktp/list/search', KtpList.as_view(), name='search_kk'),
    path('kk/create/', KkCreate.as_view(), name='create_kk'),
    path('kk/update/<pk>', KkUpdate.as_view(), name='update_kk'),
    path('kk/delete/<pk>', KkDelete.as_view(), name='delete_kk'),
    path('kk/detail/<pk>', KkDetail.as_view(), name='detail_kk'),
]
