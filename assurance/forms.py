# assurance/forms.py
from django import forms
from .models import Client, Assurance

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'  # ou spécifiez les champs: ['nom', 'prenom', 'email', ...]
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
        }

class AssuranceForm(forms.ModelForm):
    class Meta:
        model = Assurance
        fields = '__all__'
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }