from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from clients.models import Client

class Insurance(models.Model):
    TYPE_CHOICES = (
        ('auto', _('Automobile')),
        ('home', _('Habitation')),
        ('health', _('Santé')),
        ('life', _('Vie')),
        ('business', _('Entreprise')),
    )
    
    policy_number = models.CharField(_('Numéro de police'), max_length=100, unique=True)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, 
        related_name='insurances',
        verbose_name=_('Client')
    )
    type = models.CharField(_('Type'), max_length=20, choices=TYPE_CHOICES)
    start_date = models.DateField(_('Date d\'effet'))
    end_date = models.DateField(_('Date d\'expiration'))
    premium = models.DecimalField(_('Prime'), max_digits=10, decimal_places=2)
    description = models.TextField(_('Description'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, 
        null=True, related_name='created_insurances'
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Assurance')
        verbose_name_plural = _('Assurances')
    
    def __str__(self):
        return f"{self.get_type_display()} - {self.client.name} ({self.policy_number})"
    
    @property
    def is_active(self):
        from django.utils import timezone
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date
    
    @property
    def days_to_expiration(self):
        from django.utils import timezone
        today = timezone.now().date()
        if today > self.end_date:
            return 0
        return (self.end_date - today).days