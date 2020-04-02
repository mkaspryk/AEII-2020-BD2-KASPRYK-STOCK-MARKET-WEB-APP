
from django.urls import path
from . import views

urlpatterns = [
    path('adminArea',views.adminArea, name="adminArea"),
]
