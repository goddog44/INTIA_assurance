import random
from django.contrib.auth.models import User
from django.utils import timezone
from assurance.models import Succursale, Client, TypeAssurance, Assurance
from faker import Faker

fake = Faker('fr_FR')  # Pour des données françaises

def create_superuser():
    return User.objects.create_superuser(
        username='admin',
        email='admin@intia.com',
        password='admin123'
    )

def create_succursales():
    succursales = [
        {'nom': 'Direction Générale', 'adresse': '123 Avenue Générale, Yaoundé'},
        {'nom': 'INTIA-Douala', 'adresse': '456 Rue Commerciale, Douala'},
        {'nom': 'INTIA-Yaounde', 'adresse': '789 Boulevard du 20 Mai, Yaoundé'}
    ]
    return [Succursale.objects.create(**succ) for succ in succursales]

def create_types_assurance():
    types = [
        {'nom': 'Auto', 'description': 'Assurance automobile tous risques'},
        {'nom': 'Habitation', 'description': 'Assurance habitation complète'},
        {'nom': 'Santé', 'description': 'Couverture médicale familiale'},
        {'nom': 'Vie', 'description': 'Assurance vie et épargne'},
        {'nom': 'Responsabilité civile', 'description': 'Protection responsabilité civile'}
    ]
    return [TypeAssurance.objects.create(**t) for t in types]

def create_clients(num_clients=100, succursales=None, users=None):
    clients = []
    for _ in range(num_clients):
        client = Client.objects.create(
            prenom=fake.first_name(),
            nom=fake.last_name(),
            email=fake.email(),
            telephone=fake.phone_number(),
            succursale=random.choice(succursales),
            created_by=random.choice(users)
        )
        clients.append(client)
    return clients

def create_assurances(num_assurances=200, clients=None, types_assurance=None, users=None):
    for _ in range(num_assurances):
        date_debut = fake.date_between(start_date='-1y', end_date='today')
        Assurance.objects.create(
            client=random.choice(clients),
            type=random.choice(types_assurance),
            numero_contrat=fake.unique.bothify('CON-#####-??'),
            date_debut=date_debut,
            date_fin=fake.date_between(start_date=date_debut, end_date='+2y'),
            montant=random.randint(50000, 500000),
            created_by=random.choice(users)
        )

def run():
    print("Création de l'admin...")
    admin = create_superuser()
    
    print("Création des succursales...")
    succursales = create_succursales()
    
    print("Création des types d'assurance...")
    types_assurance = create_types_assurance()
    
    print("Création des utilisateurs...")
    users = [admin]  # Ajoutez d'autres utilisateurs si nécessaire
    
    print("Création des clients...")
    clients = create_clients(num_clients=500, succursales=succursales, users=users)
    
    print("Création des assurances...")
    create_assurances(num_assurances=1000, clients=clients, types_assurance=types_assurance, users=users)
    
    print("Peuplement de la base de données terminé!")

if __name__ == '__main__':
    run()