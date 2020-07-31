
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name="portfolio"),
    path('sell/<int:currId>', views.perform_sell, name="portfolio_sell"),
]
