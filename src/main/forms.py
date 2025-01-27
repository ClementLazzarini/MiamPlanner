from django import forms
from .models import Recipe, Ingredient, Season
from django.contrib.auth import get_user_model
from django.conf import settings


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name',
            'cooking_time',
            'servings',
            'seasons',
            'is_easy',
            'steps',
            'utensils',
            'creator',
            'is_private',
            'ingredients',
            'is_veggie',
        ]
        labels = {
            'name': 'Nom de la recette',
            'cooking_time': 'Temps de cuisson (en minutes)',
            'is_veggie': 'Plat végétarien',
            'servings': 'Nombre de portions',
            'seasons': 'Saisons',
            'is_easy': 'Recette facile',
            'is_private': 'Recette privée',
            'steps': 'Étapes',
            'utensils': 'Ustensiles nécessaires',
            'ingredients': 'Ingrédients',
        }

    # Custom validation for creator to always assign the logged-in user
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['creator'].initial = user
            self.fields['creator'].widget = forms.HiddenInput()

        # Appliquer les classes Bootstrap aux champs
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Entrez le nom de la recette',
        })
        self.fields['cooking_time'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Temps de cuisson en minutes',
        })
        self.fields['servings'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre de portions',
        })
        self.fields['seasons'].widget.attrs.update({
            'class': 'form-select',
        })
        self.fields['is_easy'].widget.attrs.update({
            'class': 'form-check-input',
        })
        self.fields['steps'].widget.attrs.update({
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Décrivez les étapes de préparation',
        })
        self.fields['utensils'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ustensiles nécessaires',
        })
        self.fields['ingredients'].widget.attrs.update({
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Liste des ingrédients',
        })
        self.fields['is_private'].widget.attrs.update({
            'class': 'form-check-input',
        })
        self.fields['is_veggie'].widget.attrs.update({
            'class': 'form-check-input',
        })

        # Erreurs personnalisées
        self.fields['name'].error_messages = {
            'required': 'Le nom de la recette est obligatoire.',
        }

    # Custom validation for rating
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating and not (1 <= rating <= 5):
            raise forms.ValidationError("La note doit être entre 1 et 5.")
        return rating
