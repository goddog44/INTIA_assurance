from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User

class Client(models.Model):
    BRANCH_CHOICES = User.BRANCH_CHOICES
    
    name = models.CharField(_('Nom complet'), max_length=255)
    email = models.EmailField(_('Email'), unique=True)
    phone = models.CharField(_('Téléphone'), max_length=20)
    address = models.TextField(_('Adresse'))
    branch = models.CharField(_('Succursale'), max_length=20, choices=BRANCH_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, 
        null=True, related_name='created_clients'
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')
    
    def __str__(self):
        return self.name
    
    @property
    def branch_display(self):
        return dict(self.BRANCH_CHOICES).get(self.branch, self.branch)
    
    @property
    def insurance_count(self):
        return self.insurances.count()