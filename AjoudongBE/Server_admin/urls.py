from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('management/', views.management, name="management"),
    path('advertisement/', views.advertisement, name="advertisement"),
]