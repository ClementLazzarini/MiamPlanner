from django.contrib import admin
from .models import WeekPlan


@admin.register(WeekPlan)
class WeekPlanAdmin(admin.ModelAdmin):
    list_display = ('start_date',)
    search_fields = ('start_date',)
