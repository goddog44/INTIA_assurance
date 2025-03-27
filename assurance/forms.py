from django import forms
from .models import Client, Assurance, Succursale, TypeAssurance
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    SUCCURSALE_CHOICES = [
        ('Direction Générale', 'Direction Générale'),
        ('INTIA-Douala', 'INTIA-Douala'),
        ('INTIA-Yaounde', 'INTIA-Yaounde'),
    ]
    
    succursale = forms.ChoiceField(
        choices=SUCCURSALE_CHOICES,
        label="Succursale",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['prenom', 'nom', 'email', 'telephone', 'succursale']
        labels = {
            'prenom': 'Prénom',
            'telephone': 'Téléphone'
        }

class AssuranceForm(forms.ModelForm):
    class Meta:
        model = Assurance
        fields = ['client', 'type', 'numero_contrat', 'date_debut', 'date_fin', 'montant']
        labels = {
            'numero_contrat': 'Numéro de contrat',
            'date_debut': 'Date de début',
            'date_fin': 'Date de fin'
        }
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }