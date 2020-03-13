
from django.urls import path
from . import views

urlpatterns = [
    path('crypto_stock',views.crypto_stock, name="crypto_stock"),
]
