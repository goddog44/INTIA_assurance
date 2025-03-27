from rest_framework import serializers
from clients.models import Client
from insurances.models import Insurance
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    branch_display = serializers.CharField(source='get_branch_display', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'branch', 'branch_display']

class ClientSerializer(serializers.ModelSerializer):
    branch_display = serializers.CharField(source='branch_display', read_only=True)
    insurance_count = serializers.IntegerField(read_only=True)
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone', 'address', 'branch', 
                  'branch_display', 'created_at', 'updated_at', 
                  'created_by', 'insurance_count']
        read_only_fields = ['created_at', 'updated_at', 'created_by']

class InsuranceSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    created_by = UserSerializer(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    days_to_expiration = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Insurance
        fields = ['id', 'policy_number', 'client', 'client_name', 'type', 
                  'type_display', 'start_date', 'end_date', 'premium', 
                  'description', 'created_at', 'updated_at', 'created_by',
                  'is_active', 'days_to_expiration']
        read_only_fields = ['created_at', 'updated_at', 'created_by']