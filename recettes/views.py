from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recette
from .forms import RecetteForm

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

# --- Fin du CRUD ---