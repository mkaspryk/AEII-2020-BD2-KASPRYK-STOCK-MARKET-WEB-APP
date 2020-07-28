
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('currencies/', include('currencies.urls')),
    path('register/', include('register.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('', include('login.urls')),
    path('', include('crypto_stock.urls')),
    path('', include('quick_purchase.urls')),
    path('', include('home.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('', include('crypto_guilds.urls')),
    path('', include('adminArea.urls'))
]
