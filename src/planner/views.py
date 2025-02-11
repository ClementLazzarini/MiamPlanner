import random
from datetime import timedelta, date
from django.shortcuts import render, redirect, get_object_or_404
from .models import WeekPlan, DayPlan
from main.models import Recipe
from .forms import GeneratePlanForm

# Mapping pour relier le jour de la semaine (0 = lundi, …, 6 = dimanche)
DAY_MAPPING = {
    0: 'MONDAY',
    1: 'TUESDAY',
    2: 'WEDNESDAY',
    3: 'THURSDAY',
    4: 'FRIDAY',
    5: 'SATURDAY',
    6: 'SUNDAY',
}


def generate_week_plan(request):
    if request.method == 'POST':
        form = GeneratePlanForm(request.POST)
        if form.is_valid():
            selected_tags = form.cleaned_data.get('tags', [])
            today = date.today()
            # Calcul du lundi de la semaine en cours
            start = today - timedelta(days=today.weekday())
            week_plan, created = WeekPlan.objects.get_or_create(start_date=start)
            # Parcourir chacun des 7 jours de la semaine
            for i in range(7):
                current_date = start + timedelta(days=i)
                day_plan, created = DayPlan.objects.get_or_create(week_plan=week_plan, date=current_date)
                # Pour chaque repas (lunch et dinner)
                for meal in ['lunch', 'dinner']:
                    # Construction du nom du champ correspondant, par exemple "MONDAY_LUNCH"
                    form_field = f"{DAY_MAPPING[i]}_{meal.upper()}"
                    generate_meal = form.cleaned_data.get(form_field, False)
                    if generate_meal:
                        # Filtrer les recettes en fonction des tags sélectionnés
                        recipes = Recipe.objects.all()
                        for tag in selected_tags:
                            recipes = recipes.filter(tags__name__iexact=tag)
                        # Choisir une recette aléatoirement si au moins une est trouvée
                        if recipes.exists():
                            chosen_recipe = random.choice(list(recipes))
                        else:
                            chosen_recipe = None
                    else:
                        chosen_recipe = None

                    if meal == 'lunch':
                        day_plan.lunch = chosen_recipe
                    else:
                        day_plan.dinner = chosen_recipe
                day_plan.save()
            return redirect('planner:week_plan_detail', week_plan_id=week_plan.id)
    else:
        form = GeneratePlanForm()
    return render(request, 'planner/generate_plan.html', {'form': form})


def week_plan_detail(request, week_plan_id):
    week_plan = get_object_or_404(WeekPlan, id=week_plan_id)
    day_plans = week_plan.day_plans.order_by('date')
    return render(request, 'planner/week_plan_detail.html', {'week_plan': week_plan, 'day_plans': day_plans})
