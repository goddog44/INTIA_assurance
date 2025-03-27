from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    BRANCH_CHOICES = (
        ('headquarter', _('Direction Générale')),
        ('douala', _('INTIA-Douala')),
        ('yaounde', _('INTIA-Yaoundé')),
    )
    
    branch = models.CharField(
        _('Succursale'),
        max_length=20,
        choices=BRANCH_CHOICES,
        default='headquarter'
    )
    
    def __str__(self):
        return f"{self.username} ({self.get_branch_display()})"