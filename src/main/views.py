from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from .models import Recipe
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "main/home.html")


@login_required()
def my_recipes(request):
    recipes = Recipe.objects.filter(creator=request.user)
    context = {
        'recipes': recipes
    }
    return render(request, "main/my_recipes.html", context)


@login_required()
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('my_recipes')  # Rediriger vers une page de liste des recettes ou une autre vue
    else:
        form = RecipeForm(user=request.user)

    return render(request, "main/create_recipe.html", {'form': form})


@login_required()
def view_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, "main/view_recipe.html", {"recipe": recipe})


@login_required()
def delete_recipe(request):
    return render(request, "main/delete_recipe.html")
