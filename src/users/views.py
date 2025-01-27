from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.shortcuts import render, redirect
from users.models import CustomUser
from users.utils import is_password_strong


def signup(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Un compte avec cet email existe déjà.")
            return redirect('signup')

        if not email or not password:
            messages.error(request, "Veuillez entrer une adresse email et un mot de passe.")
            return redirect('signup')

        # Vérification de la robustesse du mot de passe
        password_is_strong, error_message = is_password_strong(password)
        if not password_is_strong:
            messages.error(request, error_message)
            return redirect('signup')

        # Création du compte
        CustomUser.objects.create_user(email=email, password=password)
        user = authenticate(request, email=email, password=password)

        # Connexion de l'utilisateur
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Un problème est survenu lors de la connexion après l'inscription.")
            return redirect('signup')

    return render(request, 'users/signup.html')


def login(request):
    next_url = request.GET.get('next', None)

    # Ajouter plusieurs URLs à vérifier
    exempt_urls = ['/my_recipes/', '/create_recipe/', '/modify_recipe/', 'delete_recipe']

    if next_url:
        if any(url in next_url for url in exempt_urls):
            messages.error(request, "Veuillez vous connecter pour accéder à cette page.")
            print(messages)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Veuillez entrer à la fois un email et un mot de passe.")
            return redirect('login')

        user = authenticate(request, email=email, password=password)

        # Connexion de l'utilisateur
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Échec de la connexion. Veuillez vérifier vos identifiants.")
            return redirect('login')

    return render(request, 'users/login.html')


def logout(request):
    auth_logout(request)
    return redirect('home')


def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('home')
    return render(request, 'users/delete_account.html')
