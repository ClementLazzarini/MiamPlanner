from django.urls import path
from . import views

urlpatterns = [
    # R (Read) - La liste des recettes
    path('', views.RecetteListView.as_view(), name='recette_list'),
    
    # R (Read) - Le détail d'une recette
    path('recette/<int:pk>/', views.RecetteDetailView.as_view(), name='recette_detail'),
    
    # C (Create) - La page pour créer une recette
    path('recette/creer/', views.RecetteCreateView.as_view(), name='recette_creer'),
    
    # U (Update) - La page pour modifier une recette
    path('recette/<int:pk>/modifier/', views.RecetteUpdateView.as_view(), name='recette_modifier'),
    
    # D (Delete) - La page pour supprimer une recette
    path('recette/<int:pk>/supprimer/', views.RecetteDeleteView.as_view(), name='recette_supprimer'),

    # Garde ton générateur si tu veux
    #path('generateur/', views.generateur_menu, name='generateur'),
]