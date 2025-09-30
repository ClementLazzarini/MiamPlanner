from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my_recipes/', views.my_recipes, name='my_recipes'),
    path('create_recipe/', views.create_or_edit_recipe, name='create_recipe'),
    path('search-ingredients/', views.search_ingredients, name='search_ingredients'),
    path('add-ingredient/', views.add_ingredient_to_recipe, name='add_ingredient_to_recipe'),
    path('edit_recipe/<uuid:id>/', views.create_or_edit_recipe, name='edit_recipe'),
    path('view_recipe/<uuid:id>/', views.view_recipe, name='view_recipe'),
    path('delete_recipe/<uuid:id>/', views.delete_recipe, name='delete_recipe')
]
