from django.urls import path
from . import views

urlpatterns = [
    path('', views.insurance_list, name='insurance_list'),
    path('<int:pk>/', views.insurance_detail, name='insurance_detail'),
    path('create/', views.insurance_create, name='insurance_create'),
    path('<int:pk>/update/', views.insurance_update, name='insurance_update'),
    path('<int:pk>/delete/', views.insurance_delete, name='insurance_delete'),
]