from django import forms
from .models import Recipe


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
        widgets = {
            'is_easy': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_private': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_veggie': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'seasons': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['creator'].initial = user
            self.fields['creator'].widget = forms.HiddenInput()

        # Appliquer les classes Bootstrap aux champs
        field_classes = {
            'name': 'form-control',
            'cooking_time': 'form-control',
            'servings': 'form-control',
            'steps': 'form-control',
            'utensils': 'form-control',
            'ingredients': 'form-control',
        }

        for field, css_class in field_classes.items():
            self.fields[field].widget.attrs.update({'class': css_class})

        # Ajout des placeholders
        self.fields['name'].widget.attrs.update({'placeholder': 'Nom de la recette'})
        self.fields['cooking_time'].widget.attrs.update({'placeholder': 'Ex: 30 minutes'})
        self.fields['servings'].widget.attrs.update({'placeholder': 'Ex: 4 personnes'})
        self.fields['steps'].widget.attrs.update({'placeholder': 'Décrivez les étapes ici...', 'rows': 5})
        self.fields['utensils'].widget.attrs.update({'placeholder': 'Listez les ustensiles nécessaires'})
        self.fields['ingredients'].widget.attrs.update({'placeholder': 'Listez les ingrédients...', 'rows': 4})

