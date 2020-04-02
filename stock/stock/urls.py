
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('portfolio.urls')),
    path('',include('adminArea.urls')),
    path('',include('userArea.urls')),
    path('',include('crypto_stock.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
