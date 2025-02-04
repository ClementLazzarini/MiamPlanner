from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

# Définir les choix pour la saison
SEASON_CHOICES = [
    ('Hiver', 'Hiver'),
    ('Printemps', 'Printemps'),
    ('Été', 'Été'),
    ('Automne', 'Automne')
]

# Définir les choix pour la saison
CATEGORY_CHOICES = [
    ('Entrée', 'Entrée'),
    ('Plat Principal', 'Plat Principal'),
    ('Dessert', 'Dessert')
]


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price_per_kg = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='ingredients/', null=True, blank=True)
    season = models.CharField(
        max_length=20,
        choices=SEASON_CHOICES,
        null=True,
        blank=True
    )
    is_halal = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    # Identifiant unique pour lier la recette à une BDD générale
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        help_text="Identifiant unique pour lier la recette à une BDD générale"
    )
    name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        null=True,
        blank=True
    )
    image = models.ImageField(null=True, blank=True)
    difficulty = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="Note entre 1 et 5",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    preparation_time = models.PositiveIntegerField(help_text="Temps de cuisson en minutes", default=0)
    cooking_time = models.PositiveIntegerField(help_text="Temps de cuisson en minutes", default=0)
    is_veggie = models.BooleanField(default=False)
    servings = models.PositiveIntegerField()
    # Gestion de plusieurs saisons
    seasons = models.ManyToManyField(
        'Season',
        related_name="recipes",
        blank=True,
        help_text="Saisons associées à la recette"
    )
    is_easy = models.BooleanField(default=False)
    steps = models.TextField(default="False")
    utensils = models.TextField()
    rating = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="Note entre 1 et 5",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    # L'utilisateur qui a créé la recette, la recette reste même si l'utilisateur est supprimé
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="recipes",
        help_text="L'utilisateur qui a créé cette recette"
    )
    is_private = models.BooleanField(default=False)
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création
    updated_at = models.DateTimeField(auto_now=True)  # Date de modification

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=20, unique=True, choices=SEASON_CHOICES)

    def __str__(self):
        return self.name
