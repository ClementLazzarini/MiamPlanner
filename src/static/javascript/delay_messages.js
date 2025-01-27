function delay_messages() {
    // Sélectionne tous les éléments avec la classe "message"
    var messages = document.querySelectorAll('.message');

    // Applique un délai avant de masquer chaque message
    setTimeout(function() {
        messages.forEach(function(message) {
            // Applique l'effet de disparition
            message.style.transition = "opacity 1s";
            message.style.opacity = 0;

            // Après l'effet de fondu, masque complètement l'élément
            setTimeout(function() {
                message.style.display = 'none';
            }, 1000); // Correspond au temps de la transition (1 seconde)
        });
    }, 3000); // Délai de 3 secondes avant que les messages commencent à disparaître
}

document.addEventListener("DOMContentLoaded", function() {
    delay_messages(); // Appelle la fonction delay_messages une fois que le DOM est complètement chargé
});
