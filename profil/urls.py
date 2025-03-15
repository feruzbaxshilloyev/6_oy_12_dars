from django.urls import path
from .views import *

app_name = 'profil'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', profil_view, name='profil'),
    path('account/', account, name='account'),
]
