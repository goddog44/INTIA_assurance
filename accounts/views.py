from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomAuthenticationForm, UserRegistrationForm
from .models import User

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            branch = form.cleaned_data.get('branch')
            user = authenticate(username=username, password=password)
            if user is not None:
                # Update user branch if different
                if user.branch != branch:
                    user.branch = branch
                    user.save()
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from clients.models import Client
        from insurances.models import Insurance
        import datetime
        
        # Get counts for dashboard
        context['client_count'] = Client.objects.all().count()
        context['insurance_count'] = Insurance.objects.all().count()
        
        # Get renewals count (insurances expiring in the next 30 days)
        today = datetime.date.today()
        thirty_days = today + datetime.timedelta(days=30)
        context['renewal_count'] = Insurance.objects.filter(
            end_date__range=[today, thirty_days]
        ).count()
        
        # Get recent activity
        recent_clients = Client.objects.order_by('-created_at')[:3]
        recent_insurances = Insurance.objects.order_by('-created_at')[:3]
        
        # Combine and sort by created_at
        recent_activity = []
        for client in recent_clients:
            recent_activity.append({
                'type': 'client',
                'object': client,
                'created_at': client.created_at
            })
        
        for insurance in recent_insurances:
            recent_activity.append({
                'type': 'insurance',
                'object': insurance,
                'created_at': insurance.created_at
            })
        
        recent_activity.sort(key=lambda x: x['created_at'], reverse=True)
        context['recent_activity'] = recent_activity[:5]
        
        return context