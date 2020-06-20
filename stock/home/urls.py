
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #path('unban',views.unban, name="unban"),
    path('register',views.register, name="register"),
    path('login',views.login, name="login"),
    path('resetPassword',views.resetPassword, name="resetPassword"),
    path('logout',views.logout, name="logout"),
    #path('set_admin',views.set_admin, name="set_admin"),
    #path('remove_admin',views.remove_admin, name="remove_admin"),
    #path('ban_hammer',views.ban_hammer, name="ban_hammer"),
]
