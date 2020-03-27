
from django.urls import path
from . import views
from . import simpleexample
urlpatterns = [
    path('crypto_stock',views.crypto_stock, name="crypto_stock"),
]
