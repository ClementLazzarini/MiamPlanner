from django.urls import path
from . import views

app_name = 'planner'

urlpatterns = [
    path('generate_week_plan/', views.generate_week_plan, name='generate_week_plan'),
    path('week/<int:week_plan_id>/', views.week_plan_detail, name='week_plan_detail'),
]
