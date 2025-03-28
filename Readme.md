# Système de Gestion d'Assurance INTIA

## 🏢 Introduction

Le système de gestion d'assurance INTIA est une application web complète conçue pour la société INTIA Assurance. Cette plateforme centralise la gestion des clients et des contrats d'assurance à travers différentes succursales, notamment :
- Direction Générale
- INTIA-Douala
- INTIA-Yaoundé

## ✨ Fonctionnalités Principales

### 🔐 INTIA Dashboard
- **Authentification et Gestion des Utilisateurs**
  - Connexion sécurisée avec choix de la succursale
  - Gestion des droits d'accès basée sur les rôles

### 👥 Gestion des Clients
- Ajout, modification et suppression de clients
- Recherche et filtrage avancés
- Visualisation détaillée des informations clients

### 📋 Gestion des Contrats d'Assurance
- Création et gestion des polices d'assurance
- Suivi des dates d'échéance et des renouvellements
- Types d'assurance multiples : 
  - Auto
  - Habitation
  - Santé
  - Et plus encore...

### 📊 Tableau de Bord Analytique
- Statistiques sur les clients et contrats
- Suivi des activités récentes
- Alertes pour les contrats à renouveler

## 🚀 Technologies Utilisées

### Backend
- **Framework:** Django 4.2 (Python)
- **API:** Django REST Framework
- **Base de données:** PostgreSQL

### Frontend
- **Technologies:** HTML5, CSS3, JavaScript
- **Framework CSS:** TailwindCSS
- **Design:** Responsive (compatible mobile)

## 🛠️ Installation

### Prérequis
- Python 3.9+
- PostgreSQL 13+
- Git

### Étapes d'Installation

1. **Cloner le Dépôt 📂**
   ```bash
   git clone https://github.com/votre-nom/intia-insurance.git
   cd intia-insurance
   ```

2. **Créer et Activer un Environnement Virtuel 💽**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. **Configurer la Base de Données 💿**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Installer les Dépendances 📦**
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   ```

5. **Creer un super utilisateur 🦹‍♂️**
   _NB: -Le nom
       -mot de passe
       -email sont obligatoires lors de la creation_
```bash
python manage.py createsuperuser
```

6. **Lancer le Serveur**
   ```bash
   python manage.py runserver
   ```

## 🌟 Amélioration de l'Efficacité

Ce système est conçu pour améliorer l'efficacité des opérations d'assurance et simplifier la gestion des données clients et des contrats. Il offre une interface utilisateur intuitive et sécurisée pour gérer les clients et les contrats d'assurance à travers plusieurs succursales.

---

**Développé par INTIA Assurance** 📈🔒
