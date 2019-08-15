from django.urls import path
from akun.views import loginview, logoutView


app_name = 'akun'

urlpatterns = [
    path('login/', loginview, name='login'),
    path('logout/', logoutView, name='logout'),
]
