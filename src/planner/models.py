# planner/models.py

from django.db import models
from main.models import Recipe


class WeekPlan(models.Model):
    start_date = models.DateField(
        unique=True,
        help_text="Date du lundi de la semaine concernée"
    )
    # Si ton planning doit être propre à un utilisateur, ajoute par exemple :
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Planning de la semaine commençant le {self.start_date}"


class DayPlan(models.Model):
    week_plan = models.ForeignKey(
        WeekPlan,
        on_delete=models.CASCADE,
        related_name='day_plans'
    )
    date = models.DateField(help_text="Date de ce jour")
    # Ces champs peuvent rester null s’il n’y a pas de suggestion pour ce repas
    lunch = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lunch_plans'
    )
    dinner = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='dinner_plans'
    )

    def __str__(self):
        return f"{self.date} - Midi: {self.lunch} / Soir: {self.dinner}"
