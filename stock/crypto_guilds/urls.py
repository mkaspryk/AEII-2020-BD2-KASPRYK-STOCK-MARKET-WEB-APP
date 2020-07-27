
from django.urls import path
from . import views

urlpatterns = [
    path('crypto_guilds',views.crypto_guilds, name="crypto_guilds"),
]
