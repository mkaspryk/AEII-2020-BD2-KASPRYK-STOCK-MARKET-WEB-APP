
from django.urls import path
from . import views

urlpatterns = [
    path('guild_creation',views.guild_creation, name="guild_creation"),
]
