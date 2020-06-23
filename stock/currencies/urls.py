from django.urls import path
from . import views

urlpatterns = [
    path('prices.json', views.prices, name="prices"),
]
