from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('perform_quick_buy/', views.perform_quick_buy),
]
