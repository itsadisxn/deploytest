# food/urls.py
from django.conf.urls import url
from django.urls import path
from food import views


urlpatterns = [
    path('food/', views.index, name='index'),
]