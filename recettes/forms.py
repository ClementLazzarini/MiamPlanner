from django import forms
from .models import Recette

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        # On dit au formulaire quels champs on veut
        fields = ['nom', 'temps_preparation', 'temps_cuisson', 'ingredients', 'etapes', 'tags']

        # Par défaut, les tags s'affichent mal.
        # Ceci les transforme en jolies cases à cocher.
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }