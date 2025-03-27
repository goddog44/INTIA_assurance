from django import forms
from django.utils import timezone
from .models import Insurance

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ['policy_number', 'client', 'type', 'start_date', 'end_date', 'premium', 'description']
        widgets = {
            'policy_number': forms.TextInput(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'premium': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set default dates if creating a new instance
        if not self.instance.pk:
            today = timezone.now().date()
            next_year = today.replace(year=today.year + 1)
            self.fields['start_date'].initial = today
            self.fields['end_date'].initial = next_year
        
        # Filter client choices based on user's branch
        if user and user.branch != 'headquarter':
            self.fields['client'].queryset = self.fields['client'].queryset.filter(branch=user.branch)