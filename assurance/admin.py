from django.contrib import admin
from .models import Client, Insurance, Branch, InsuranceType

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(InsuranceType)
class InsuranceTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'branch')
    list_filter = ('branch',)
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('contract_number', 'client', 'insurance_type', 'start_date', 'end_date', 'amount')
    list_filter = ('insurance_type', 'start_date')
    search_fields = ('contract_number', 'client__first_name', 'client__last_name')