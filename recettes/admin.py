from django.contrib import admin
from .models import Recette, Tag


class RecetteAdmin(admin.ModelAdmin):
    # Ceci va créer une belle boîte de sélection "double"
    # C'est la meilleure interface pour les ManyToManyField
    filter_horizontal = ('tags',)


admin.site.register(Recette, RecetteAdmin)
admin.site.register(Tag)