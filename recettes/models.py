from django.db import models


class Tag(models.Model):
    nom = models.CharField(max_length=100, unique=True) # "unique=True" évite les doublons

    def __str__(self):
        return self.nom
    

class Recette(models.Model):
    nom = models.CharField(max_length=255)
    
    temps_preparation = models.IntegerField(default=0)
    temps_cuisson = models.IntegerField(default=0)
    
    ingredients = models.TextField(
        blank=True,
        help_text="Mettez un ingrédient par ligne (ex: 2 courgettes)"
    )
    
    etapes = models.TextField(blank=True)
    
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.nom

    # Une petite propriété utile pour ton filtre "rapide"
    @property
    def temps_total(self):
        return self.temps_preparation + self.temps_cuisson