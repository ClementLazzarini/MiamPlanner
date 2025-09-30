from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from .models import Recipe, Ingredient
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string


def home(request):
    public_recipes = Recipe.objects.filter(is_private=False)

    # Sélectionner 3 recettes aléatoires si elles existent
    recipes = list(public_recipes.order_by('?')[:3])  # '?' = aléatoire
    context = {
        'recipes': recipes
    }
    return render(request, "main/home.html", context)


def search_ingredients(request):
    query = request.GET.get('q', '')
    print(f"Requête reçue : {query}")
    ingredients = Ingredient.objects.filter(name__icontains=query)[:10]  # Limite à 10 résultats
    return render(request, 'main/ingredient_list.html', {'ingredients': ingredients})


def add_ingredient_to_recipe(request):
    ingredient_id = request.POST.get('ingredient_id')
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)

    # Récupérer la liste des ingrédients en session
    selected_ingredients = request.session.get('selected_ingredients', [])

    # Ajouter l'ingrédient si pas déjà présent
    if ingredient_id not in selected_ingredients:
        selected_ingredients.append(ingredient_id)
        request.session['selected_ingredients'] = selected_ingredients  # Mettre à jour la session
        request.session.modified = True

    # Retourne l'affichage dynamique de l'ingrédient ajouté
    return HttpResponse(f'<li>{ingredient.name}</li>')


@login_required()
def my_recipes(request):
    recipes = Recipe.objects.filter(creator=request.user)
    context = {
        'recipes': recipes
    }
    return render(request, "main/my_recipes.html", context)


def create_or_edit_recipe(request, id=None):
    """
    Gère la création et la modification d'une recette.
    - Si recipe_id est fourni, on modifie une recette existante.
    - Sinon, on crée une nouvelle recette.
    """
    # Récupérer la recette si l'ID est fourni, sinon None
    recipe = get_object_or_404(Recipe, id=id) if id else None

    if request.method == 'POST':
        # Utilisation du formulaire avec instance (pour modification)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            # Récupérer les ingrédients temporairement stockés en session
            selected_ingredients = request.session.get('selected_ingredients', [])

            # Associer ces ingrédients à la recette
            for ingredient_id in selected_ingredients:
                ingredient = get_object_or_404(Ingredient, id=ingredient_id)
                recipe.ingredients.add(ingredient)

            # Nettoyer la session après l'enregistrement
            request.session['selected_ingredients'] = []
            request.session.modified = True
            return redirect('my_recipes', recipe.id)  # Redirige vers la liste des recettes
    else:
        # Pré-remplir le formulaire si une recette existe
        form = RecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'main/create_recipe.html', context)


@login_required()
def view_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, "main/view_recipe.html", {"recipe": recipe})


@login_required()
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        recipe.delete()
        messages.success(request, f"La recette '{recipe.name}' a été supprimée avec succès.")
        return redirect('my_recipes')

    return render(request, "main/delete_recipe.html", {"recipe": recipe})
