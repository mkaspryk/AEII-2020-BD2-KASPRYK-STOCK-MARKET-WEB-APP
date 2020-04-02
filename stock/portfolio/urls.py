
from django.urls import path
from . import views

urlpatterns = [
    path('portfolio', views.portfolio, name="portfolio"),
    path('welcome', views.welcome, name="welcome"),
    path('profile', views.profile, name="profile"),
    path('stock', views.stock, name="stock"),
    path('clan', views.clan, name="clan"),
]
