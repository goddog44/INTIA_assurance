from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Q
from .serializers import ClientSerializer, InsuranceSerializer
from clients.models import Client
from insurances.models import Insurance

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Client.objects.all().annotate(
            insurance_count=Count('insurances')
        ).order_by('-created_at')
        
        # Filter by search query
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | 
                Q(email__icontains=search) |
                Q(phone__icontains=search)
            )
        
        # Filter by branch if not headquarters
        if self.request.user.branch != 'headquarter':
            queryset = queryset.filter(branch=self.request.user.branch)
            
        return queryset
    
    def perform_create(self, serializer):
        # If not headquarters, set branch to user's branch
        if self.request.user.branch != 'headquarter':
            serializer.save(created_by=self.request.user, branch=self.request.user.branch)
        else:
            serializer.save(created_by=self.request.user)

class InsuranceViewSet(viewsets.ModelViewSet):
    serializer_class = InsuranceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Insurance.objects.all().order_by('-created_at')
        
        # Filter by search query
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(policy_number__icontains=search) | 
                Q(client__name__icontains=search) |
                Q(type__icontains=search)
            )
        
        # Filter by type
        insurance_type = self.request.query_params.get('type', None)
        if insurance_type:
            queryset = queryset.filter(type=insurance_type)
        
        # Filter by branch if not headquarters
        if self.request.user.branch != 'headquarter':
            queryset = queryset.filter(client__branch=self.request.user.branch)
            
        return queryset
    
    def perform_create(self, serializer):
        # Verify client belongs to user's branch if not headquarters
        client = serializer.validated_data['client']
        if self.request.user.branch != 'headquarter' and client.branch != self.request.user.branch:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Vous n'avez pas accès à ce client.")
            
        serializer.save(created_by=self.request.user)