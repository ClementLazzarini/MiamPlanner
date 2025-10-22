from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Recette, Tag
from .forms import RecetteForm
from django.shortcuts import render
from django.utils import timezone

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
def get_current_season():
    """Devine la saison actuelle (pour l'hémisphère nord)."""
    now = timezone.now()
    month = now.month
    
    if month in (12, 1, 2):
        return 'Hiver'
    elif month in (3, 4, 5):
        return 'Printemps'
    elif month in (6, 7, 8):
        return 'Été'
    else:  # 9, 10, 11
        return 'Automne'

# Fonction principale du générateur de recettes
def get_random_recipe(criteres):
    """
    Piocher une recette au hasard en fonction de critères.
    'criteres' est un dict, ex: {'tags': ['rapide', 'été']}
    """
    
    queryset = Recette.objects.all()
    
    if criteres.get('tags'):
        tags_a_filtrer = criteres['tags']
        
        for tag_nom in tags_a_filtrer:
            queryset = queryset.filter(tags__nom__iexact=tag_nom)
            
    recette_choisie = queryset.order_by('?').distinct().first()
    
    return recette_choisie


class GenerateurMenuView(View):
    template_name = 'recettes/generateur.html'
    
    # On définit les listes ici pour les réutiliser
    JOURS_LISTE = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    REPAS_LISTE = ['Midi', 'Soir']
    TAGS_SAISON = ['Hiver', 'Printemps', 'Été', 'Automne']

    def get(self, request):
        tous_les_tags = Tag.objects.all()

        saison_actuelle = get_current_season()
        
        contexte = {
            'tous_les_tags': tous_les_tags,
            'jours_liste': self.JOURS_LISTE,
            'repas_liste': self.REPAS_LISTE, 
            'tags_saison_lower': [tag.lower() for tag in self.TAGS_SAISON],
            'saison_actuelle_lower': saison_actuelle.lower()
        }
        return render(request, self.template_name, contexte)
    
    def post(self, request):
        tous_les_tags = Tag.objects.all()
        menu_genere = {}
        
        repas_semaine = []
        menu_simple_json = {}
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
                nom_propre = repas_id.replace('_', ' ').title()
                data = menu_genere.get(nom_propre, {}) # On récupère les données
                recette = data.get('recette')
                
                if recette:
                    # Si on a une recette, on stocke son nom et son URL
                    menu_simple_json[nom_propre] = {
                        'nom': recette.nom,
                        'url': reverse('recette_detail', kwargs={'pk': recette.pk})
                    }
                elif f'{repas_id}_idee' in request.POST:
                    # Si on a demandé une idée mais qu'on n'a rien trouvé
                    menu_simple_json[nom_propre] = {
                        'nom': f"(Aucune recette trouvée {data.get('tags_filtres', '')})",
                        'url': None
                    }
                else:
                    # Si on n'a pas demandé d'idée
                    menu_simple_json[nom_propre] = None
        
        saison_actuelle = get_current_season()

        contexte = {
            'menu_genere': menu_genere,
            'tous_les_tags': tous_les_tags,
            'jours_liste': self.JOURS_LISTE,
            'repas_liste': self.REPAS_LISTE,
            'tags_saison_lower': [tag.lower() for tag in self.TAGS_SAISON],
            'saison_actuelle_lower': saison_actuelle.lower(),
            'menu_simple_json': menu_simple_json
        }
        return render(request, self.template_name, contexte)


def mon_menu_view(request):
    """Affiche la page qui lira le menu depuis le localStorage."""
    return render(request, 'recettes/mon_menu.html')