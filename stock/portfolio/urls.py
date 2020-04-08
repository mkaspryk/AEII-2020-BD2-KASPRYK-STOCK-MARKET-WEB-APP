
from django.urls import path
from . import views

urlpatterns = [
    path('portfolio', views.portfolio, name="portfolio"),
    path('welcome', views.welcome, name="welcome"),
]
