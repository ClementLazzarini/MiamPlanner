from django import forms
from .models import Recette

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        # On dit au formulaire quels champs on veut
        fields = ['nom', 'temps_preparation', 'temps_cuisson', 'ingredients', 'etapes', 'tags', 'lien_source']

        # Par défaut, les tags s'affichent mal.
        # Ceci les transforme en jolies cases à cocher.
        widgets = {
            # On définit une classe CSS standard pour les inputs
            'nom': forms.TextInput(attrs={
                'class': 'bg-white mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm'
            }),
            'temps_preparation': forms.NumberInput(attrs={
                'class': 'bg-white mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm'
            }),
            'temps_cuisson': forms.NumberInput(attrs={
                'class': 'bg-white mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm'
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'bg-white mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm',
                'rows': 5
            }),
            'etapes': forms.Textarea(attrs={
                'class': 'bg-white mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm',
                'rows': 8
            }),
            'lien_source': forms.URLInput(attrs={
                'class': 'bg-white mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm'
            }),
            
            # Pour les tags, on garde le widget de base
            # car tu le styles manuellement dans le template (ce qui est la bonne méthode)
            'tags': forms.CheckboxSelectMultiple,
        }