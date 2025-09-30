from django.contrib import admin
from .models import Ingredient, Recipe, Season, Tag


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_kg', 'is_halal', 'season', 'image_preview')
    list_filter = ('is_halal', 'season')
    search_fields = ('name',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-width: 100px; max-height: 100px;" />'
        return "Pas d'image"
    image_preview.allow_tags = True
    image_preview.short_description = "Aperçu de l'image"


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'cooking_time', 'is_veggie', 'rating', 'is_private', 'created_at')
    list_filter = ('is_veggie', 'is_private', 'seasons', 'rating')
    search_fields = ('name', 'creator__email', 'creator__username')
    autocomplete_fields = ('ingredients', 'creator', 'seasons')  # Facilite la recherche dans les champs liés
    readonly_fields = ('created_at', 'updated_at')  # Pour éviter de modifier les champs de date
    filter_horizontal = ('ingredients', 'tags',)  # Améliore l'interface pour les relations ManyToMany

    fieldsets = (
        ('Informations Générale', {
            'fields': ('name', 'category', 'image', 'creator', 'cooking_time', 'servings', 'is_veggie', 'rating', 'is_private')
        }),
        ("Saisonnalité et Ingrédients", {
            'fields': ('seasons', 'ingredients')
        }),
        ("Instructions", {
            'fields': ('steps', 'utensils')
        }),
        ("Dates", {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
