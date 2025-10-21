from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Recette, Tag
from .forms import RecetteForm
from django.shortcuts import render

# --- Le CRUD ---

# R (Read) - Liste
class RecetteListView(ListView):
    model = Recette
    # Par défaut, Django cherche un template appelé :
    # recette_list.html (ou, dans notre cas, recettes/recette_list.html)
    # Il envoie la liste dans une variable "object_list"

# R (Read) - Détail
class RecetteDetailView(DetailView):
    model = Recette
    # Par défaut, Django cherche : recettes/recette_detail.html
    # Il envoie la recette dans une variable "object"

# C (Create) - Création
class RecetteCreateView(CreateView):
    model = Recette
    form_class = RecetteForm  # On lui dit d'utiliser notre formulaire
    template_name = 'recettes/recette_form.html' # On va créer ce template
    success_url = reverse_lazy('recette_list') # Où aller après succès

# U (Update) - Modification
class RecetteUpdateView(UpdateView):
    model = Recette
    form_class = RecetteForm
    template_name = 'recettes/recette_form.html' # Réutilise le même template !
    success_url = reverse_lazy('recette_list')

# D (Delete) - Suppression
class RecetteDeleteView(DeleteView):
    model = Recette
    success_url = reverse_lazy('recette_list')
    template_name = 'recettes/recette_confirm_delete.html' # Page de confirmation


# --- Le Générateur de Menu ---

# Fonction principale du générateur de recettes
def get_random_recipe(criteres):
    """
    Piocher une recette au hasard en fonction de critères.
    'criteres' est un dict, ex: {'tags': ['rapide', 'été']}
    """
    
    queryset = Recette.objects.all()
    
    if criteres.get('tags'):
        tags_a_filtrer = criteres['tags']
        
        # On enchaîne les .filter() pour chaque tag demandé
        # C'est un "ET" logique (rapide ET été)
        for tag_nom in tags_a_filtrer:
            queryset = queryset.filter(tags__nom__iexact=tag_nom)
            
    recette_choisie = queryset.order_by('?').distinct().first()
    
    return recette_choisie


class GenerateurMenuView(View):
    template_name = 'recettes/generateur.html'
    
    # On définit les listes ici pour les réutiliser
    JOURS_LISTE = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    REPAS_LISTE = ['Midi', 'Soir']

    def get(self, request):
        tous_les_tags = Tag.objects.all()
        
        contexte = {
            'menu_genere': {},
            'tous_les_tags': tous_les_tags,
            'jours_liste': self.JOURS_LISTE,  # <-- On envoie la liste
            'repas_liste': self.REPAS_LISTE   # <-- On envoie la liste
        }
        return render(request, self.template_name, contexte)
    
    def post(self, request):
        tous_les_tags = Tag.objects.all()
        menu_genere = {}
        
        # On génère la liste des ID (ex: 'lundi_midi') dynamiquement !
        repas_semaine = []
        for jour in self.JOURS_LISTE:
            for repas in self.REPAS_LISTE:
                repas_semaine.append(f"{jour.lower()}_{repas.lower()}")

        for repas_id in repas_semaine:
            if f'{repas_id}_idee' in request.POST:
                criteres = {}
                tags_coches = request.POST.getlist(f'{repas_id}_tags')
                
                if tags_coches:
                    criteres['tags'] = tags_coches
                
                recette = get_random_recipe(criteres)
                nom_propre_du_repas = repas_id.replace('_', ' ').title()
                menu_genere[nom_propre_du_repas] = {
                    'recette': recette,
                    'tags_filtres': tags_coches
                }
        
        contexte = {
            'menu_genere': menu_genere,
            'tous_les_tags': tous_les_tags,
            'jours_liste': self.JOURS_LISTE, # <-- On les renvoie aussi
            'repas_liste': self.REPAS_LISTE
        }
        return render(request, self.template_name, contexte)