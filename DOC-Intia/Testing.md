# Stratégie de Test

## 1. Tests Unitaires
- Validation des modèles (Client, Assurance)
- Tests des formulaires
- Logique métier

## 2. Tests d'Intégration
- Workflow complet client/assurance
- Authentification utilisateur
- Contrôle d'accès par succursale

## 3. Tests Fonctionnels
```python
# Exemple de test
class ClientTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            prenom="Jean",
            nom="Dupont",
            email="jean.dupont@example.com",
            telephone="+237612345678"
        )

    def test_client_creation(self):
        self.assertEqual(self.client.nom_complet(), "Jean Dupont")