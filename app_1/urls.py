from django.urls import path
from .views import *

app_name = 'app1'
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('details/<int:id>/', details, name='details'),
    path('create/', Create.as_view(), name='create'),
    path('contact', contact, name='contact'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]
