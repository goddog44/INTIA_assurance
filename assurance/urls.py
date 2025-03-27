from django.urls import path
from assurance import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    
    # Clients URLs
    path('clients/', views.clients, name='clients'),
    path('clients/new/', views.client_create, name='client_create'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),
    
    # Insurances URLs
    path('insurances/', views.insurances, name='insurances'),
    path('insurances/new/', views.insurance_create, name='insurance_create'),
    path('insurances/<int:pk>/', views.insurance_detail, name='insurance_detail'),
    path('insurances/<int:pk>/delete/', views.insurance_delete, name='insurance_delete'),
    
    # API endpoint
    path('api/clients/', views.get_clients_json, name='get_clients_json'),
]