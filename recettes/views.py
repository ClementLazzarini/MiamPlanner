from django.shortcuts import render
from .models import Recette  # Importe ton modèle !

def home(request):
    """Home view displaying all recipes.

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    toutes_les_recettes = Recette.objects.all()

    contexte = {
        'recettes': toutes_les_recettes
    }

    return render(request, 'recettes/liste_recettes.html', contexte)