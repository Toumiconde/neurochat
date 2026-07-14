# On importe AbstractUser — le modèle User de base de Django
# Il contient déjà : username, password, email, is_active...
from django.contrib.auth.models import AbstractUser

# On importe models — l'outil pour créer les colonnes de la table
from django.db import models

# On crée notre modèle User qui hérite d'AbstractUser
# Hériter = on garde tout ce qu'AbstractUser a + on ajoute nos champs
class User(AbstractUser):

    # Email unique — sera utilisé pour la connexion
    # unique=True = deux users peuvent pas avoir le même email
    email = models.EmailField(unique=True)

    # Nom affiché dans le chat (peut être différent du vrai nom)
    # max_length = maximum 100 caractères
    display_name = models.CharField(max_length=100)

    # Photo de profil — stockée dans le dossier avatars/
    # blank=True, null=True = optionnel, peut être vide
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # Courte description de l'utilisateur
    bio = models.CharField(max_length=500, blank=True, null=True)

    # Plan de l'utilisateur — free, premium ou pro
    # choices = liste des valeurs autorisées
    PLAN_CHOICES = [
        ('free', 'Gratuit'),
        ('premium', 'Premium'),
        ('pro', 'Pro'),
    ]
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default='free')

    # Email vérifié ou pas — False par défaut à l'inscription
    is_verified = models.BooleanField(default=False)

    # Comment l'user s'est inscrit — email ou google
    AUTH_PROVIDER_CHOICES = [
        ('email', 'Email'),
        ('google', 'Google'),
    ]
    auth_provider = models.CharField(max_length=20, choices=AUTH_PROVIDER_CHOICES, default='email')

    # Compteur de messages envoyés aujourd'hui
    # Pour gérer les quotas du plan gratuit
    daily_message_count = models.IntegerField(default=0)

    # Date de la dernière réinitialisation du compteur
    last_count_reset = models.DateField(blank=True, null=True)

    # Date de création du compte — auto_now_add = rempli automatiquement
    created_at = models.DateTimeField(auto_now_add=True)

    # Date de dernière modification — auto_now = mis à jour automatiquement
    updated_at = models.DateTimeField(auto_now=True)

    # On dit à Django d'utiliser l'email pour la connexion
    # Au lieu du username par défaut
    USERNAME_FIELD = 'email'

    # Les champs obligatoires à la création d'un superuser
    REQUIRED_FIELDS = ['username', 'display_name']

    # Représentation textuelle de l'objet User
    # Quand Django affiche un user → il montre son email
    def __str__(self):
        return self.email