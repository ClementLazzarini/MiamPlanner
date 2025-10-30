// On récupère la liste des tags de saison (en minuscules)
const seasonTags = JSON.parse(document.getElementById('season-tags-data').textContent);

// --- 1. FONCTION POUR SAUVEGARDER LES "IDÉES" ---
function savePreferences() {
    const inputs = document.querySelectorAll('input[id$="_idee"]');
    inputs.forEach(input => {
        localStorage.setItem(input.id, input.checked);
    });
}

// --- 2. FONCTION POUR CHARGER LES "IDÉES" ---
function loadPreferences() {
    const inputs = document.querySelectorAll('input[id$="_idee"]');
    inputs.forEach(input => {
        const savedValue = localStorage.getItem(input.id);
        if (savedValue !== null) {
            input.checked = (savedValue === 'true');
        }
    });
}

function initSeasonTagLogic() {
    // On sélectionne TOUTES les checkboxes de tags
    const allTagCheckboxes = document.querySelectorAll('input[name$="_tags"]');

    allTagCheckboxes.forEach(checkbox => {
    checkbox.addEventListener('change', (e) => {
    const clickedCheckbox = e.target;
    const clickedTag = clickedCheckbox.value.toLowerCase();

    // Si la case cochée n'est PAS une saison, on ne fait rien
    if (!seasonTags.includes(clickedTag)) {
        return;
    }

    // Si on a coché une saison, on trouve son "groupe"
    // (ex: 'lundi_midi_tags')
    const groupName = clickedCheckbox.name;

    // On récupère toutes les autres cases du MÊME groupe
    document.querySelectorAll(`input[name="${groupName}"]`).forEach(siblingCheckbox => {
        // On ne touche pas à la case qu'on vient de cliquer
        if (siblingCheckbox === clickedCheckbox) {
            return;
        }

        // Si une autre case du groupe est aussi une saison...
        const siblingTag = siblingCheckbox.value.toLowerCase();
        if (seasonTags.includes(siblingTag)) {
            // ... on la DÉCOCHE !
            siblingCheckbox.checked = false;
        }
    });
    });
    });
}

document.addEventListener('DOMContentLoaded', (event) => {

    const menuDataElement = document.getElementById('menu-data-to-save');
    
    // N'oubliez pas de récupérer les tags de saison ici, en haut du 'DOMContentLoaded'
    // car 'initSeasonTagLogic' en a besoin
    const seasonTagsElement = document.getElementById('season-tags-data');
    const seasonTags = seasonTagsElement ? JSON.parse(seasonTagsElement.textContent) : [];


    if (menuDataElement) {
        // --- PARTIE REDIRECTION ---
        
        // On a généré un menu, on le sauvegarde !
        const menuData = JSON.parse(menuDataElement.textContent);
        localStorage.setItem('savedMenu', JSON.stringify(menuData));
        
        // --- LA CORRECTION EST ICI ---
        // 1. On trouve le formulaire
        const form = document.querySelector('form');
        // 2. On lit l'URL depuis son attribut data-
        const redirectUrl = form.dataset.redirectUrl;

        // 3. On redirige vers la bonne URL !
        window.location.href = redirectUrl;

    } else {
        // --- PARTIE NORMALE (pas de redirection) ---
        
        // Charge les préférences des cases "Idée"
        loadPreferences();
        
        // Active la logique "radio" pour les tags de saison
        // Assurez-vous que 'seasonTags' est défini (voir ajout en haut)
        if (seasonTags.length > 0) {
            initSeasonTagLogic(seasonTags); // Passez les tags à la fonction
        }

        // Met en place la sauvegarde des cases "Idée"
        const form = document.querySelector('form');
        form.addEventListener('change', (e) => {
            // On ne sauvegarde que si on a changé une case "Idée"
            if (e.target.id.endsWith('_idee')) {
                savePreferences();
            }
        });
    }
});