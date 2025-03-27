Système de Gestion d'Assurance INTIA
====================================

Introduction
Le système de gestion d'assurance INTIA est une application web complète conçue pour la société INTIA Assurance. Cette plateforme centralise la gestion des clients et des contrats d'assurance à travers différentes succursales, notamment la Direction Générale, INTIA-Douala et INTIA-Yaoundé.

Fonctionnalités Principales
INTIA Dashboard
Authentification et Gestion des Utilisateurs:

Connexion sécurisée avec choix de la succursale.

Gestion des droits d'accès basée sur les rôles.

Gestion des Clients:

Ajout, modification et suppression de clients.

Recherche et filtrage avancés.

Visualisation détaillée des informations clients.

Gestion des Contrats d'Assurance:

Création et gestion des polices d'assurance.

Suivi des dates d'échéance et des renouvellements.

Types d'assurance multiples : Auto, Habitation, Santé, etc.

Tableau de Bord Analytique:

Statistiques sur les clients et contrats.

Suivi des activités récentes.

Alertes pour les contrats à renouveler.

Technologies Utilisées
Backend
Django 4.2 (Framework Python)

Django REST Framework (API RESTful)

PostgreSQL (Base de données)

Frontend
HTML5, CSS3, JavaScript

TailwindCSS (Framework CSS)

Design Responsive (compatible mobile)

Installation
Prérequis
Python 3.9+

PostgreSQL 13+

Git

Étapes d'Installation
Cloner le Dépôt Git:

bash
git clone https://github.com/votre-nom/intia-insurance.git
cd intia-insurance
Créer et Activer un Environnement Virtuel Python:

bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
Faire des Migrations du Schéma de la BD:

bash
python manage.py makemigrations
Appliquer les Modifications:

bash
python manage.py migrate
Installer les Dépendances:

bash
pip install -r requirements.txt
Appliquer les Migrations (encore une fois après installation des dépendances):

bash
python manage.py migrate
Lancer le Serveur:

bash
python manage.py runserver
Amélioration de l'Efficacité
Ce système est conçu pour améliorer l'efficacité des opérations d'assurance et simplifier la gestion des données clients et des contrats. Il offre une interface utilisateur intuitive et sécurisée pour gérer les clients et les contrats d'assurance à travers plusieurs succursales.