# urls.py

from django.urls import path
from homeWork1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
