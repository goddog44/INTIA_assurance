from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='dashboard'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('clients/', include('clients.urls')),
    path('insurances/', include('insurances.urls')),
    path('api/', include('api.urls')),
]