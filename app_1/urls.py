from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('news/', news, name='news'),
    path('details/<int:id>/', details, name='details'),
    path('create/', create, name='create'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]
