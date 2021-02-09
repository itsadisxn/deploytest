# food/urls.py
from django.conf.urls import url
from django.urls import path
from cake import views


urlpatterns = [
    path('cake/', views.index, name='index'),
]