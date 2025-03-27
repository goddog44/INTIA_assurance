from django.urls import path
from assurance import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Authentification
    path('connexion/', views.login_view, name='login'),
    path('deconnexion/', views.logout_view, name='logout'),
    
    # Tableau de bord
    path('', login_required(views.tableau_de_bord), name='tableau_de_bord'),
    
    # Clients
    path('clients/', 
         login_required(views.liste_clients), 
         name='liste_clients'),
    path('clients/nouveau/', 
         login_required(views.creer_client), 
         name='creer_client'),
    path('clients/<int:pk>/', 
         login_required(views.detail_client), 
         name='detail_client'),
    path('clients/<int:pk>/modifier/', 
         login_required(views.modifier_client), 
         name='modifier_client'),
    path('clients/<int:pk>/supprimer/', 
         login_required(views.supprimer_client), 
         name='supprimer_client'),
    
    # Assurances
    path('assurances/', 
         login_required(views.liste_assurances), 
         name='liste_assurances'),
    path('assurances/nouvelle/', 
         login_required(views.creer_assurance), 
         name='creer_assurance'),
    path('assurances/<int:pk>/', 
         login_required(views.modifier_assurance), 
         name='modifier_assurance'),
    path('assurances/<int:pk>/supprimer/', 
         login_required(views.supprimer_assurance), 
         name='supprimer_assurance'),
    
    # API
    path('api/clients/', 
         login_required(views.get_clients_json), 
         name='get_clients_json'),
]