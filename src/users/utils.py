import re


def is_password_strong(password):
    # Vérification si le mot de passe est assez long
    if len(password) < 8:
        return False, "Le mot de passe doit contenir au moins 8 caractères."

    # Combinaison de plusieurs vérifications en une seule expression régulière
    pattern = r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>])'

    # Vérification avec l'expression régulière
    if not re.search(pattern, password):
        errors = []
        if not re.search(r'[A-Z]', password):
            errors.append("une lettre majuscule")
        if not re.search(r'[0-9]', password):
            errors.append("un chiffre")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append("un caractère spécial")

        # Construction d'un message d'erreur personnalisé
        error_message = "Le mot de passe doit contenir " + ", ".join(errors) + "."
        return False, error_message

    # Vérification des espaces inutiles
    if password.strip() != password:
        return False, "Le mot de passe ne doit pas contenir d'espaces au début ou à la fin."

    return True, ""
