
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #path('unban',views.unban, name="unban"),

    #path('set_admin',views.set_admin, name="set_admin"),
    #path('remove_admin',views.remove_admin, name="remove_admin"),
    #path('ban_hammer',views.ban_hammer, name="ban_hammer"),
]
