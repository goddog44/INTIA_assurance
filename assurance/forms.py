from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Client, Insurance, Branch, InsuranceType

class LoginForm(AuthenticationForm):
    BRANCH_CHOICES = [
        ('Direction Générale', 'Direction Générale'),
        ('INTIA-Douala', 'INTIA-Douala'), 
        ('INTIA-Yaounde', 'INTIA-Yaounde'),
    ]
    
    branch = forms.ChoiceField(
        choices=BRANCH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full p-2 border rounded text-base text-gray-900 dark:text-gray-100 bg-white dark:bg-gray-700 border-gray-300 dark:border-gray-600'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'w-full p-2 border rounded text-base text-gray-900 dark:text-gray-100 bg-white dark:bg-gray-700 border-gray-300 dark:border-gray-600'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'w-full p-2 border rounded text-base text-gray-900 dark:text-gray-100 bg-white dark:bg-gray-700 border-gray-300 dark:border-gray-600'
        })

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'branch']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'w-full p-2 border rounded text-base text-gray-900 dark:text-gray-100 bg-white dark:bg-gray-700 border-gray-300 dark:border-gray-600'
            })

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ['client', 'insurance_type', 'contract_number', 'start_date', 'end_date', 'amount']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'w-full p-2 border rounded text-base text-gray-900 dark:text-gray-100 bg-white dark:bg-gray-700 border-gray-300 dark:border-gray-600'
            })
        
        # Set date input type
        self.fields['start_date'].widget.input_type = 'date'
        self.fields['end_date'].widget.input_type = 'date'