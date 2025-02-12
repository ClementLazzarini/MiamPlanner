# A lancer via le terminal avec =>
# python manage.py shell < DATA/import_ingredients_from_xml.py
import xml.etree.ElementTree as ET
from main.models import Ingredient
from django.core.exceptions import ObjectDoesNotExist

# Charger et analyser le fichier XML
tree = ET.parse('DATA/alim_2020_07_07.xml')  # Remplace par le chemin de ton fichier XML
root = tree.getroot()

# Parcourir chaque élément ALIM et extraire les données
for alim in root.findall('ALIM'):
    alim_nom_fr = alim.find('ALIM_NOM_INDEX_FR').text

    # Créer l'ingrédient uniquement avec le nom
    ingredient, created = Ingredient.objects.get_or_create(
        name=alim_nom_fr
    )

    if created:
        print(f"Ajouté : {alim_nom_fr}")
    else:
        print(f"Déjà existant : {alim_nom_fr}")

print("Importation terminée ! ✅")
