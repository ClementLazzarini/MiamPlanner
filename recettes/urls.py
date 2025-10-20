from django.urls import path
from recettes.views import home

urlpatterns = [
    path('', home, name='home'),
]