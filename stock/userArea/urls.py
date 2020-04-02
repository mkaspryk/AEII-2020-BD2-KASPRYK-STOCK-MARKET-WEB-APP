
from django.urls import path
from . import views

urlpatterns = [
    path('userArea',views.userArea, name="userArea"),
]
