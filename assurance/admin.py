from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Succursale, Client, TypeAssurance, Assurance

@admin.register(Succursale)
class SuccursaleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'nombre_clients')
    search_fields = ('nom', 'adresse')
    
    def nombre_clients(self, obj):
        count = obj.client_set.count()
        # Update this line to use your actual app name and URL pattern name
        url = reverse("admin:assurance_client_changelist") + f"?succursale__id__exact={obj.id}"
        return format_html('<a href="{}">{} Clients</a>', url, count)
    nombre_clients.short_description = "Nombre de clients"

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'email', 'telephone', 'lien_succursale', 'nombre_assurances')
    list_filter = ('succursale',)
    search_fields = ('prenom', 'nom', 'email', 'telephone')
    
    def nom_complet(self, obj):
        return f"{obj.prenom} {obj.nom}"
    nom_complet.short_description = "Nom complet"
    
    def lien_succursale(self, obj):
        url = reverse("admin:assurance_succursale_change", args=[obj.succursale.id])
        return format_html('<a href="{}">{}</a>', url, obj.succursale.nom)
    lien_succursale.short_description = "Succursale"
    
    def nombre_assurances(self, obj):
        count = obj.assurance_set.count()
        url = reverse("admin:assurance_assurance_changelist") + f"?client__id__exact={obj.id}"
        return format_html('<a href="{}">{} Assurances</a>', url, count)
    nombre_assurances.short_description = "Assurances"

@admin.register(Assurance)
class AssuranceAdmin(admin.ModelAdmin):
    list_display = ('numero_contrat', 'client_info', 'type_assurance', 'date_debut', 'date_fin')
    
    def client_info(self, obj):
        url = reverse("admin:assurance_client_change", args=[obj.client.id])
        return format_html('<a href="{}">{} {}</a>', url, obj.client.prenom, obj.client.nom)
    client_info.short_description = "Client"
    
    def type_assurance(self, obj):
        url = reverse("admin:assurance_typeassurance_change", args=[obj.type.id])
        return format_html('<a href="{}">{}</a>', url, obj.type.nom)
    type_assurance.short_description = "Type d'assurance"

@admin.register(TypeAssurance)
class TypeAssuranceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'nombre_assurances')
    
    def nombre_assurances(self, obj):
        count = obj.assurance_set.count()
        url = reverse("admin:assurance_assurance_changelist") + f"?type__id__exact={obj.id}"
        return format_html('<a href="{}">{} Assurances</a>', url, count)
    nombre_assurances.short_description = "Nombre d'assurances"