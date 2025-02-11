import random
from main.models import Recipe


def generate_planning(user):
    user_pref = UserPreference.objects.get(user=user)
    meal_plan = []

    for day in ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]:
        for meal_type in ["breakfast", "lunch", "dinner"]:
            preference = user_pref.meal_preferences.get(f"{day}_{meal_type}", "default")

            if preference == "pas besoin":
                continue  # Ignore ce repas

            # Filtrer les recettes en fonction de la préférence
            recipes = Recipe.objects.all()
            if preference == "végé":
                recipes = recipes.filter(category="végé")
            elif preference == "repas facile":
                recipes = recipes.filter(difficulty="facile")

            chosen_recipe = recipes.order_by("?").first()  # Choix aléatoire

            if chosen_recipe:
                meal_plan.append({
                    "day": day,
                    "meal_type": meal_type,
                    "recipe": chosen_recipe
                })

    return meal_plan

