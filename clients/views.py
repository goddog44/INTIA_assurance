from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Client
from .forms import ClientForm
from insurances.models import Insurance

@login_required
def client_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        clients = Client.objects.filter(
            Q(name__icontains=search_query) | 
            Q(email__icontains=search_query) |
            Q(phone__icontains=search_query)
        )
    else:
        clients = Client.objects.all()
    
    # Filter by user's branch unless they're from headquarters
    if request.user.branch != 'headquarter':
        clients = clients.filter(branch=request.user.branch)
    
    return render(request, 'clients/client_list.html', {
        'clients': clients,
        'search_query': search_query
    })

@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    insurances = Insurance.objects.filter(client=client)
    
    # Check if user has access to this client
    if request.user.branch != 'headquarter' and request.user.branch != client.branch:
        messages.error(request, "Vous n'avez pas accès à ce client.")
        return redirect('client_list')
    
    return render(request, 'clients/client_detail.html', {
        'client': client,
        'insurances': insurances
    })

@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            
            # If not headquarters, set branch to user's branch
            if request.user.branch != 'headquarter':
                client.branch = request.user.branch
                
            client.save()
            messages.success(request, "Client ajouté avec succès.")
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
        
        # Pre-select branch based on user's branch
        if request.user.branch != 'headquarter':
            form.fields['branch'].initial = request.user.branch
            form.fields['branch'].widget.attrs['disabled'] = True
    
    return render(request, 'clients/client_form.html', {
        'form': form,
        'title': 'Ajouter un client'
    })

@login_required
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    
    # Check if user has access to this client
    if request.user.branch != 'headquarter' and request.user.branch != client.branch:
        messages.error(request, "Vous n'avez pas accès à ce client.")
        return redirect('client_list')
    
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            # If not headquarters, ensure branch stays the same
            if request.user.branch != 'headquarter':
                form.instance.branch = client.branch
                
            form.save()
            messages.success(request, "Client modifié avec succès.")
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
        
        # Disable branch field if not headquarters
        if request.user.branch != 'headquarter':
            form.fields['branch'].widget.attrs['disabled'] = True
    
    return render(request, 'clients/client_form.html', {
        'form': form,
        'client': client,
        'title': 'Modifier un client'
    })

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    
    # Check if user has access to this client
    if request.user.branch != 'headquarter' and request.user.branch != client.branch:
        messages.error(request, "Vous n'avez pas accès à ce client.")
        return redirect('client_list')
    
    # Check if client has insurances
    if client.insurance_count > 0:
        messages.error(request, "Impossible de supprimer ce client car il a des assurances associées.")
        return redirect('client_detail', pk=client.pk)
    
    if request.method == 'POST':
        client.delete()
        messages.success(request, "Client supprimé avec succès.")
        return redirect('client_list')
    
    return render(request, 'clients/client_confirm_delete.html', {
        'client': client
    })