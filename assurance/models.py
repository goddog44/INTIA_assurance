from django.db import models
from django.contrib.auth.models import User

class Succursale(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    
    def __str__(self):
        return self.nom

class Client(models.Model):
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    succursale = models.ForeignKey(Succursale, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

class TypeAssurance(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        verbose_name = "Type d'assurance"
        verbose_name_plural = "Types d'assurance"

class Assurance(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")
    type = models.ForeignKey(TypeAssurance, on_delete=models.CASCADE, verbose_name="Type d'assurance")
    numero_contrat = models.CharField(max_length=50, unique=True, verbose_name="Numéro de contrat")
    date_debut = models.DateField(verbose_name="Date de début")
    date_fin = models.DateField(verbose_name="Date de fin")
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Assurance"
        verbose_name_plural = "Assurances"